---
title: Contents
---

**Computational Analysis of Sound Scenes and Events**
(CASSE) is a book edited by Tuomas Virtanen (Tampere University of Technology), Mark Plumbley (University of Surrey), and Dan Ellis (Google Inc.).

This web site provides online resources associated with the book.

Note: In the list below, only some chapter names link to associated content.  The other chapters have no online content for the moment.

### Chapters

{% assign grouped = site.docs | group_by: 'category' %}
{% for group in grouped %}
{% assign items = group.items | sort: 'order' %}
{% if site.chapters contains group.name %}
* {{ group.name }} [{{ items.first.title }}]({{ site.baseurl }}{{ items.first.url }})
{% else %}
* {{ group.name }} {{ items.first.title }}
{% endif %}
{% endfor %}
