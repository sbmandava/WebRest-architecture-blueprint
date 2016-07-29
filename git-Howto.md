# Quick Howto #

### Download/Clone the Git App and upload changes ##

The URL can be found at https://bitbucket.org/copperiq/videoplatform

```
mkdir git
cd git
git clone https://github.com/sbmandava/WebRest-architecture-blueprint.git 
```

first time when you run it, it will prompt id/password and stores it locally.

```
cd user-application
```

** Now makes changes as you like to the files. **

when the changes are done. Tell the system what changed.

```
git add <file_name> : will add the specific file
git add .  : will add all files and folders which got changed
git add <directory>/ : will add a directory and subdirectory 
```
   
* Add comment to what the change is, so people know what to expect

```
   git commit . -m "added data directory"
```

* Now Commit(Upload) the changes

```
   git push origin master
```

### Next time, make sure you Pull ###

Next time you are in the folder, make sure you pull the changes done by other users. (Rather than cloning everything)

``` 
   git pull
```

* To see the status of git

```
   git status
``` 
   
### Things to be aware off.

* All code is version controlled, so changes are captured for analysis
* Add good comments to your code, so it's easier to understand.
* Feel free to try new ideas, don't worry about failure.
