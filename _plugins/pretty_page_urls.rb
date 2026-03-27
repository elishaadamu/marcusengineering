# Automatically generates pretty (directory-style) URLs for service pages
# in the industries, applications, and expertise directories.
#
# Without this, Jekyll outputs e.g. /industries/aerospace-v1.0.html
# but navigation links expect /industries/aerospace-v1.0/
# This plugin bridges that gap so pages are output as /industries/aerospace-v1.0/index.html

Jekyll::Hooks.register :pages, :post_init do |page|
  # Don't override explicit permalinks
  next if page.data['permalink']

  # Only target pages in these specific directories
  next unless page.relative_path.match?(/\A(industries|applications|expertise)\//)

  # Skip index pages (they already resolve correctly)
  next if page.name == 'index.markdown' || page.name == 'index.md'

  basename = File.basename(page.name, File.extname(page.name))
  dir = File.dirname(page.relative_path)
  page.data['permalink'] = "/#{dir}/#{basename}/"
end
