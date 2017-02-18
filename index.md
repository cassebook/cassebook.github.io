---
category: Contents
---

**Computational Analysis of Sound Scenes and Events**
(CASSE) is a book edited by Tuomas Virtanen (Tampere University of Technology), Mark Plumbley (University of Surrey), and Dan Ellis (Google Inc.).

This web site provides online resources associated with the book.

### Chapters

{% assign grouped = site.docs | group_by: 'category' %}
{% for group in grouped %}
{% assign items = group.items | sort: 'order' %}
* {{ group.name }} [{{ items.first.title }}]({{ site.baseurl }}{{ items.first.url }})
{% endfor %}
