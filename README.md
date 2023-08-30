# Advanced Git Practice
> A workshop for practicing/learning `git`, specifically tackling:
* branching/merging
* merge conflicts
* stashing
* cherry picking
* rebasing

Resources:
* [Git Internals (pdf book)](https://raw.githubusercontent.com/pluralsight/git-internals-pdf/master/drafts/peepcode-git.pdf)
  * [related video/presentation](https://www.youtube.com/watch?v=P6jD966jzlk)

## Workshop Guide:

````bash
# first clone this repository, enter its folder
#   (optionally, you can fork this repo on github and then clone it)
git clone git@github.com:dangbert/git-workshop.git
cd git-workshop
````

Now open `practice.py` and ensure you understand what the 3 functions inside do.


````bash
# check which branch you're on (should be "main")
git branch

# see what other branches exist on Github as well
git branch --all
````

The `refactor-compare` branch differs from main by one commit. We're gonna merge them.