This is a testing repo for some network script I am working on.  This is a learning exercise.  None of this is meant for any production use.

### Roadmap:
  - Multi-session (multithreading?)
    - Currently, the script conncets to hosts one at a time. For this to be useful for pulling information from many devices, I would like it to do all, or a set number of sessions simultaneously.
  - Error handling
    - Outside of a basic validity check of the IPs passed, there is nothing to handle errors
  - Clean exiting
  - Generate .txt files with outputs for each session
    - Maybe something like {datetime}_{hostname}.txt
