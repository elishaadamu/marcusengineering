#!/usr/bin/env ruby
# frozen_string_literal: true

require "net/http"
require "uri"

MAX_REDIRECTS = 10

def normalize_url(url)
  uri = URI.parse(url)
  uri.fragment = nil

  path = uri.path.to_s
  path = "/" if path.empty?
  path = path.sub(%r{/+\z}, "")
  path = "/" if path.empty?
  uri.path = path

  uri.to_s
rescue URI::InvalidURIError
  url
end

def fetch_with_redirects(source_url, max_redirects: MAX_REDIRECTS)
  uri = URI.parse(source_url)
  seen = {}
  redirects = 0
  final_response = nil

  loop do
    current = uri.to_s
    raise "Redirect loop detected at #{current}" if seen[current]

    seen[current] = true

    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = (uri.scheme == "https")
    http.open_timeout = 10
    http.read_timeout = 15
    http.write_timeout = 10 if http.respond_to?(:write_timeout=)

    request = Net::HTTP::Get.new(uri.request_uri)
    request["User-Agent"] = "backlink-redirect-test/1.0"
    response = http.request(request)
    final_response = response

    unless response.is_a?(Net::HTTPRedirection)
      return [response.code.to_i, uri.to_s, redirects]
    end

    location = response["location"]
    raise "Redirect without location header from #{current}" if location.nil? || location.empty?

    redirects += 1
    raise "Too many redirects for #{source_url}" if redirects > max_redirects

    uri = URI.join(uri, location)
  end
rescue StandardError => e
  [0, "", 0, e.message]
end

redirect_map_file = ARGV[0] || "tests/backlinks-redirects.tsv"

unless File.file?(redirect_map_file)
  warn "FAIL: Redirect map file not found: #{redirect_map_file}"
  exit 1
end

rows = []

File.foreach(redirect_map_file, chomp: true) do |line|
  stripped = line.strip
  next if stripped.empty? || stripped.start_with?("#")

  source_url, expected_final_url = stripped.split("\t", 2)
  if source_url.nil? || expected_final_url.nil? || source_url.empty? || expected_final_url.empty?
    warn "FAIL: Invalid row in #{redirect_map_file}: #{line}"
    exit 1
  end

  rows << [source_url, expected_final_url]
end

if rows.empty?
  warn "FAIL: No redirect checks were loaded from #{redirect_map_file}"
  exit 1
end

failures = 0
unique_final_urls = {}

rows.each do |source_url, expected_final_url|
  status_code, final_url, redirect_count, error = fetch_with_redirects(source_url)

  if error
    puts "FAIL: #{source_url} -> #{error}"
    failures += 1
    next
  end

  if redirect_count < 1
    puts "FAIL: #{source_url} -> expected at least one redirect, got #{redirect_count}"
    failures += 1
    next
  end

  normalized_final = normalize_url(final_url)
  normalized_expected = normalize_url(expected_final_url)

  if normalized_final != normalized_expected
    puts "FAIL: #{source_url} -> expected #{normalized_expected}, got #{normalized_final}"
    failures += 1
    next
  end

  unless status_code.between?(200, 399)
    puts "FAIL: #{source_url} -> final status #{status_code} is not successful"
    failures += 1
    next
  end

  unique_final_urls[normalized_final] = true
  puts "PASS: #{source_url} -> #{normalized_final} (redirects: #{redirect_count})"
end

if unique_final_urls.length < rows.length
  puts "FAIL: Backlink redirects are not independent (some targets are shared)"
  failures += 1
end

if failures.positive?
  puts "Backlink redirect test failed: #{failures} failing checks out of #{rows.length}."
  exit 1
end

puts "Backlink redirect test passed: #{rows.length} checks."