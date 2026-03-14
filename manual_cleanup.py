import os

jekyll_posts_dir = r"c:\Users\user\Documents\marcusengineering\_posts"

conflicts = [
    "2011-08-20-startup-weekend-day-1-7.markdown",
    "2011-08-21-startup-weekend-day-2-8.markdown",
    "2011-12-27-dr-marcus-leader-under-40-10.markdown",
    "2016-03-16-sarsef-reception-2016-28.markdown",
    "2017-03-12-300k-up-for-grabs-at-venture-madness-2017-30.markdown",
    "2021-12-14-marcus-engineering-small-business-of-the-year-2021-3.markdown"
]

for f in conflicts:
    path = os.path.join(jekyll_posts_dir, f)
    if os.path.exists(path):
        os.remove(path)
        print(f"Successfully removed: {f}")
    else:
        print(f"File not found, skipping: {f}")

print("Manual conflict cleanup complete.")
