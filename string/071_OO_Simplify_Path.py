# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:32:39 2016

71. Simplify Path

Total Accepted: 54293 Total Submissions: 243553 Difficulty: Medium

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

解题思路：
题目的要求是输出Unix下的最简路径，Unix文件的根目录为"/"，"."表示当前目录，".."表示上级目录。

例如：

输入1：

/../a/b/c/./.. 

输出1：

/a/b

模拟整个过程：

1. "/" 根目录

2. ".." 跳转上级目录，上级目录为空，所以依旧处于 "/"

3. "a" 进入子目录a，目前处于 "/a"

4. "b" 进入子目录b，目前处于 "/a/b"

5. "c" 进入子目录c，目前处于 "/a/b/c"

6. "." 当前目录，不操作，仍处于 "/a/b/c"

7. ".." 返回上级目录，最终为 "/a/b"


@author: zeminzhang
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        curr = '/'
        for i in path:
            if i == '..':
                if curr != '/':
                    curr = '/'.join(curr.split('/')[:-1])
                    if curr == '': curr = '/'
            elif i !='.' and i!= '':
                curr += '/'+i if curr != '/' else i
        return curr