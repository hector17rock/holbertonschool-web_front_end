# 🌐 Web Frontend Advanced Project

## 📋 Project Overview

This repository contains advanced projects for web frontend development, focusing on HTML5 and CSS3. It demonstrates progressive web development techniques, including semantic markup, responsive design, multimedia integration, and modern CSS techniques.

## 📁 Directory Structure

```plaintext
holbertonschool-web_front_end
├── CSS_advanced
│   ├── images
│   │   ├── pic-about-01.jpg
│   │   ├── pic-article-01.jpg
│   │   ├── pic-article-02.jpg
│   │   ├── pic-article-03.jpg
│   │   ├── pic-person-01.jpg
│   │   ├── pic-person-02.jpg
│   │   ├── pic-person-03.jpg
│   │   ├── pic-work-01.jpg
│   │   ├── pic-work-02.jpg
│   │   └── pic-work-03.jpg
│   ├── styles (32 CSS files)
│   └── README.md
├── html_advanced
│   ├── README.md
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── latest_news.html
│   ├── styleguide.html
│   ├── article.html
│   ├── favicon.ico
│   ├── favicon.png
│   ├── 0-39-index.html (incremental development files)
│   ├── 11-39-styleguide.html (styleguide files)
│   └── Python testing scripts (8 files)
└── README.md
```

### Directory Breakdown:

#### **🎨 CSS_advanced/** (44 files total)
- **🖼️ images/** (10 files) - High-resolution images for various website sections
- **📄 styles/** (32 files) - Progressive CSS files from `1-style.css` to `32-style.css`
- **📖 README.md** - Comprehensive documentation of CSS advanced features

#### **📝 html_advanced/** (53 files total)
- **🏠 Core Pages** (7 files) - Main website pages including index, about, contact, etc.
- **🔄 Incremental Development** (30 files) - HTML files showing progressive development from 0-index.html to 36-index.html
- **🎨 Styleguides** (8 files) - Component demonstrations and HTML element examples
- **🐍 Testing Scripts** (8 files) - Python validation and testing utilities
- **🎯 Assets** (2 files) - Favicon files for the website

## 📝 HTML Advanced Module

This module showcases the progressive development of a website using HTML5. It includes:
- 🏠 Core Page Implementations
- 🔄 Incremental Development Files (0-29)
- 🎨 Comprehensive Styleguides

Detailed file listings can be found in the `README.md` within the `html_advanced` directory.

## 🎨 CSS Advanced Module

The CSS advanced project explores modern styling capabilities, including:
- 🎯 Theming and Variables
- 🏗️ Layout and Component Styling
- ✨ Advanced CSS Features and Animations

Detailed file listings can be found in the `README.md` within the `CSS_advanced` directory.

## 🚀 Technical Features

- **🏷️ HTML5 Elements:** Usage of semantic tags, multimedia, and interactive elements
- **🎨 CSS Custom Properties:** Themable and maintainable design systems
- **📱 Responsive Design:** Mobile-first approach with flexible layouts
- **♿ Accessibility:** Proper heading hierarchy, semantic markup, and screen reader support

## 📦 Installation and Usage

To view the project:
1. 📂 Open the repository directory.
2. 🧭 Navigate to the `html_advanced` and `CSS_advanced` directories for detailed examples.
3. 🌐 Open `index.html` files in a modern web browser to view the website examples.

## 📝 HTML Documentation Usage

### 🏗️ Basic HTML Structure

All HTML files in this project follow a consistent structure:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Page Title - Techium</title>
    <meta name="description" content="Techium is a digital agency">
    <link rel="icon" type="image/x-icon" href="./favicon.ico">
    <link rel="icon" type="image/png" href="./favicon.png">
  </head>
  <body>
    <!-- Content -->
  </body>
</html>
```

### 🎯 Key HTML Elements Used

#### **🏠 Semantic Layout Elements**
- `<header>` - Page header with navigation
- `<nav>` - Navigation menus
- `<main>` - Main content area
- `<section>` - Content sections
- `<article>` - Individual articles/items
- `<footer>` - Page footer

#### **📰 Content Elements**
- `<h1>` to `<h6>` - Heading hierarchy
- `<p>` - Paragraphs
- `<ul>`, `<ol>`, `<li>` - Lists
- `<dl>`, `<dt>`, `<dd>` - Definition lists
- `<blockquote>`, `<cite>` - Quotations
- `<mark>` - Highlighted text

#### **🎨 Media Elements**
- `<img>` - Images with alt text
- `<video>` - Video player with controls
- `<audio>` - Audio player
- `<iframe>` - Embedded content

#### **📊 Data Elements**
- `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>` - Tables
- `<caption>` - Table captions
- `<details>`, `<summary>` - Collapsible content

### 🔧 HTML Usage Examples

#### **Navigation Structure**
```html
<nav>
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="#services">Services</a></li>
    <li><a href="#works">Works</a></li>
    <li><a href="#about">About</a></li>
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
```

#### **Article Structure**
```html
<article>
  <div>
    <img src="images/pic-work-01.jpg" alt="Work Example">
  </div>
  <h3><a href="#">Interior Design</a></h3>
  <p>Project description goes here...</p>
</article>
```

#### **Testimonial with Blockquote**
```html
<article>
  <img src="images/pic-person-01.jpg" alt="Client Name" width="100" height="100">
  <blockquote>
    Client testimonial text here...
    <cite>Client Name</cite>
  </blockquote>
</article>
```

#### **Video Implementation**
```html
<video src="path/to/video.mp4" controls loop poster="path/to/poster.jpg">
  Sorry, your browser doesn't support HTML5 video
</video>
```

#### **Data Table**
```html
<table>
  <caption>Star Wars Trilogy Data</caption>
  <thead>
    <tr>
      <th scope="col">Title</th>
      <th scope="col">Director</th>
      <th scope="col">Release Date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Star Wars: Episode IV - A New Hope</th>
      <td>George Lucas</td>
      <td>May 25th, 1977</td>
    </tr>
  </tbody>
</table>
```

### 📋 File Structure Guide

#### **🏠 Core Website Files**
- `index.html` - Main homepage
- `about.html` - About page
- `contact.html` - Contact page
- `latest_news.html` - News/blog page
- `article.html` - Individual article template
- `styleguide.html` - Component showcase

#### **🔄 Incremental Development Files**
- `0-index.html` to `36-index.html` - Progressive development stages
- Each file builds upon the previous, adding new features
- Shows evolution from basic HTML to complete website

#### **🎨 Styleguide Files**
- `11-styleguide.html` - Basic headings
- `26-styleguide.html` - Lists examples
- `33-styleguide.html` - Table structures
- `38-styleguide.html` - Video implementation
- `39-styleguide.html` - Audio implementation

### ♿ Accessibility Features

#### **🏷️ Semantic HTML**
- Proper heading hierarchy (h1 → h6)
- Semantic elements for screen readers
- Logical document structure

#### **🖼️ Image Accessibility**
- Alt text for all images
- Descriptive image names
- Proper image dimensions

#### **🔗 Link Accessibility**
- Descriptive link text
- Proper navigation structure
- Keyboard navigation support

#### **📊 Table Accessibility**
- Table headers with `scope` attributes
- Caption elements for context
- Proper table structure

### 📱 Mobile Optimization

#### **📏 Viewport Meta Tag**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
```

#### **🎯 SEO Optimization**
- Proper meta descriptions
- Semantic HTML structure
- Optimized title tags
- Favicon implementation

### 🧪 Testing and Validation

#### **🐍 Python Test Scripts**
- `video_check.py` - Validates video elements
- `section_check.py` - Counts HTML sections
- `test_blockquote.py` - Tests blockquote structure
- `test_table.py` - Validates table markup

#### **✅ Usage Examples**
```bash
# Run video validation
python3 video_check.py

# Check section structure
python3 section_check.py

# Test blockquote elements
python3 test_blockquote.py
```

### 🎓 Learning Path

#### **📚 Beginner Level**
1. Start with `0-index.html` - Basic HTML structure
2. Progress through `1-index.html` to `10-index.html` - Learn fundamentals
3. Explore `11-styleguide.html` - Understand headings

#### **🔧 Intermediate Level**
1. Study `12-index.html` to `20-index.html` - Page sections
2. Review `26-styleguide.html` to `33-styleguide.html` - Advanced elements
3. Practice with `about.html` and `contact.html`

#### **🚀 Advanced Level**
1. Analyze `36-index.html` - Complete implementation
2. Master `38-styleguide.html` and `39-styleguide.html` - Multimedia
3. Understand testing scripts and validation techniques

## 👨‍💻 Authors

**Hector** - *Project Developer and Maintainer*
- 🐙 GitHub: [@hector](https://github.com/hector)
- 📧 Email: [Contact Information]

## 🤝 Contributions

Contributions to improve this project are welcome. Please fork the repository and submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Developed by Hector**

*This project is part of the Holberton School curriculum, demonstrating advanced HTML5 and CSS3 practices.*
