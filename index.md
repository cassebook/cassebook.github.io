---
title: Contents
---

**Computational Analysis of Sound Scenes and Events**
(CASSE) is a book edited by Tuomas Virtanen (Tampere University of Technology), Mark Plumbley (University of Surrey), and Dan Ellis (Google Inc.).

This web site provides online resources associated with the book.

Note: In the list below, only the chapters with associated content are links.

### Chapters

{% assign grouped = site.docs | group_by: 'category' %}
{% for group in grouped %}
{% assign items = group.items | sort: 'order' %}
{% if group.name == 'Chapter  2' or group.name == 'Chapter  6' or group.name == 'Chapter  8' or group.name == 'Chapter  9' or group.name == 'Chapter 10' or group.name == 'Chapter 11' %}
* {{ group.name }} [{{ items.first.title }}]({{ site.baseurl }}{{ items.first.url }})
{% else %}
* {{ group.name }} {{ items.first.title }}
{% endif %}
{% endfor %}
