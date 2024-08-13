# Longest Substring Without Repeating Characters
## Problem
Given a string s, find the length of the longest 
substring without repeating characters.

## Solution
This is the typical sliding windows problem using an hashtable to keep the position.
Everytime that we find a duplicate charater in the window we slide the window to the next one,
we need also to check that we don't slide backward. Guidelines:
- keep a start and end position
- register any new char and its position in the hashtable.
- when found a duplicate move the start: slide the window at the position of the original + 1,
  if only if we are not going backward.


 
