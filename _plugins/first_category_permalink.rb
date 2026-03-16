# Custom permalink generator that uses only the first category
# This plugin overrides the default permalink structure to use only the first word of the first category

module Jekyll
  class FirstCategoryPermalinkGenerator < Generator
    priority :highest
    
    def generate(site)
      site.collections['posts'].docs.each do |post|
        categories = post.data['categories']
        if categories && !categories.empty?
          first_cat = categories.first
          # Get only the first word, downcase it, and remove non-word chars
          slugified_cat = first_cat.to_s.split.first.downcase.gsub(/[^\w]/, '')
          # Set the permalink explicitly
          post.data['permalink'] = "/#{slugified_cat}/#{post.data['slug']}/"
          post.data['category'] = slugified_cat
        end
      end
    end
  end
end
