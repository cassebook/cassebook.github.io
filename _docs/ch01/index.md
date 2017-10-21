---
title: Introduction to Sound Scene and Event Analysis
authors: Tuomas Virtanen, Mark Plumbley, and Dan Ellis
category: Chapter  1
order: 1
---

**THIS PAGE IS JUST A TEMPLATE!**

**FOR INFORMATION ABOUT THE BOOK SEE https://cassebook.github.io/ **




This is an example of the companion page for a chapter.  
It's written in [markdown](https://daringfireball.net/projects/markdown/syntax) which makes it easy to write content as a simple text file.

* You can have [links](http://www.google.com)

* You can include images: 
  ![Example image](/images/ch01/example.png)

* You can have code snippets:

```python
def proc(arg):
  if arg:
    print('hello world')
```

* You can directly include arbitrary HTML:

<table border="2">
    <tr>
        <td>Table cell</td>
    </tr>
</table>

## Creating your own chapter's companion page.

You can see the raw text source for this page on 
[GitHub](https://raw.githubusercontent.com/cassebook/cassebook.github.io/master/_docs/ch01/index.md).  It starts with something like this:

```text
---
title: Introduction to sound scene and event analysis
authors: Tuomas Virtanen, Mark Plumbley, and Dan Ellis
category: Chapter  1
order: 1
---
This is an example of the companion page for a chapter.  
It's written in [markdown](https://daringfireball.net/projects/markdown/syntax) which makes it easy to write content as a simple text file.
```

The block at the top between the `---` delimiters is a set of properties for 
the page, as used by the "Liquid" templating language.  The `category` field
controls how the page is sorted in the contents listing; it's possible to have more than one web page per chapter by giving them the same category.

To add a page for your chapter, you can simply prepare a plain text file 
using this page as an example, send it to me at [dpwe@google.com](mailto:dpwe@google.com), and I will add it to the site.  

If you want to experiment with what it's going to look like, you can clone 
the [cassebook.github.io repository](https://github.com/cassebook/cassebook.github.io) from GitHub, [install Jekyll](https://jekyllrb.com), and play with the site locally.

## Example code and other files

You can include linked files: 
[program1.py]({{ site.url }}/code/ch01/program1.py.html) 
([download]({{ site.url }}/code/ch01/program1.py)).  
I've used [pygmentize](http://pygments.org) 
to color the code, which will work for practically any language.

By convention, all code should go into a directory `/code/chXX/`, and
images and data go into `/images/chXX/` and `/data/chXX/` respectively. 

If you have more complicated needs, let me know.
