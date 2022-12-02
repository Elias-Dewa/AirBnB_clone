# 0x01. AirBnB clone - Web static

# Background Context

# Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

# General Requirements

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be W3C compliant and validate with W3C-Validator
- All your CSS files should be in styles folder
- All your images should be in images folder
- You are not allowed to use !important and id (#... in the CSS file)
- You are not allowed to use tags img, embed and iframe
- You are not allowed to use Javascript
- Current screenshots have been done on Chrome 56 or more.
- No cross browsers
- You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

# More Info

![image](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)

# Mandatory and advanced tasks

0. Inline styling

    Write an HTML page that displays a header and a footer.

    Layout:

        Body:
            no margin
            no padding
        Header:
            color #FF0000 (red)
            height: 70px
            width: 100%
        Footer:
            color #00FF00 (green)
            height: 60px
            width: 100%
            text Best School center vertically and horizontally
            always at the bottom at the page

    Requirements:

        You must use the header and footer tags
        You are not allowed to import any files
        You are not allowed to use the style tag in the head tag
        Use inline styling for all your tags

![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/98f4ac1b0644512ce7ae91a9e8e61e8fe174911d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=52abbed8cc7a7332848433f1743987caa80ab106897d735788f0592e4887cae0)

1. Head styling

    Write an HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

    Requirements:

        You must use the header and footer tags
        You are not allowed to import any files
        No inline styling
        You must use the style tag in the head tag
    The layout must be exactly the same as 0-index.html

2. CSS files

    Write an HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

    Requirements:

        You must use the header and footer tags
        No inline styling
        You must have 3 CSS files:
        styles/2-common.css: for global style (i.e. the body style)
        styles/2-header.css: for header style
        styles/2-footer.css: for footer style
    The layout must be exactly the same as 1-index.html

3. Zoning done!

    Write an HTML page that displays a header and footer by using CSS files (same as 2-index.html)

    Layout:

        Common:
            no margin
            no padding
            font color: #484848
            font size: 14px
            font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
            icon in the browser tab
        Header:
            color: white
            height: 70px
            width: 100%
            border bottom 1px #CCCCCC
            logo align on left and center vertically (20px space at the left)
        Footer:
            color white
            height: 60px
            width: 100%
            border top 1px #CCCCCC
            text Best School center vertically and horizontally
            always at the bottom at the page
    Requirements:

        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 3 CSS files:
            styles/3-common.css: for the global style (i.e body style)
            styles/3-header.css: for the header style
            styles/3-footer.css: for the footer style

![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/2be1eda05a0d9097c210f2d3482a59aa858c5711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b6814084254af965aa337b848c4f8851b894a9a0bf7fb52b60a3a5201f52d95c)

4. Search!

    Write an HTML page that displays a header, footer and a filters box with a search button.

    Layout: (based on 3-index.html)

        Container:
            between header and footer tags, add a div:
                classname: container
                max width 1000px
                margin top and bottom 30px - it should be 30px under the bottom of the header (screenshot)
                center horizontally
        Filter section:
            tag section
            classname filters
            inside the .container
            color white
            height: 70px
            width: 100% of the container
            border 1px #DDDDDD with radius 4px
        Button search:
            tag button
            text Search
            font size: 18px
            inside the section filters
            background color #FF5A5F
            text color #FFFFFF
            height: 48px
            width: 20% of the section filters
            no borders
            border radius: 4px
            center vertically and at 30px of the right border
            change opacity to 90% when the mouse is on the button
    Requirements:

        You must use: header, footer, section, button tags
        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 4 CSS files:
            styles/4-common.css: for the global style (body and .container styles)
            styles/3-header.css: for the header style
            styles/3-footer.css: for the footer style
            styles/4-filters.css: for the filters style
        4-index.html won’t be W3C valid, don’t worry, it’s temporary

![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f959154b0cdf1cdf71ddef04e3787ef28462793e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=31536e8c874c458ab2df8e7ef9142f4a5a720319819a577a4a29f36674fcae9a)

5. More filters

    Write an HTML page that displays a header, footer and a filters box.

    Layout: (based on 4-index.html)

        Locations and Amenities filters:
            tag: div
            classname: locations for location tag and amenities for the other
            inside the section filters (same level as the button Search)
            height: 100% of the section filters
            width: 25% of the section filters
            border right #DDDDDD 1px only for the first left filter
            contains a title:
                tag: h3
                font weight: 600
                text States or Amenities
            contains a subtitle:
                tag: h4
                font weight: 400
                font size: 14px
                text with fake contents
    Requirements:

        You must use: header, footer, section, button, h3, h4 tags
        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 4 CSS files:
            styles/4-common.css: for the global style (body and .container styles)
            styles/3-header.css: for the header style
            styles/3-footer.css: for the footer style
            styles/5-filters.css: for the filters style
![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/85bfa50b96c2985723daa75b5e22f75ef16e2b2e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3950fe04597ea40b0323c8e13ed1886a4be1f2988a5ceb6edf89e87a5120b4e0)

6. It's (h)over

    Write an HTML page that displays a header, footer and a filters box with dropdown.

    Layout: (based on 5-index.html)

        Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter div:
            tag ul
            classname popover
            text should be fake now
            inside each div
            not displayed by default
            color #FAFAFA
            width same as the div filter
            border #DDDDDD 1px with border radius 4px
            no list display
            Location filter has 2 levels of ul/li:
                state -> cities
                state name must be display in a h2 tag (font size 16px)
    Requirements:

        You must use: header, footer, section, button, h3, h4, ul, li tags
        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 4 CSS files:
            styles/4-common.css: for the global style (body and .container styles)
            styles/3-header.css: for the header style
            styles/3-footer.css: for the footer style
            styles/6-filters.css: for the filters style
![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6262f13624dca23ca19db505c44f88faddb82ebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=68dc11fee39114210abee369c435bf65fddcd5a4a32f172ece7a19f660b56cad)
![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6e6bdfa13fa88a5f439d9e2b1dade826dd95529b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c2b6e12e485c55c49fb94845e1ed350f20c16244e3b07ff63d56c765962beba3)

7. Display results

    Write an HTML page that displays a header, footer, a filters box with dropdown and results.

    Layout: (based on 6-index.html)

        Add Places section:
            tag: section
            classname: places
            same level as the filters section, inside .container
            contains a title:
                tag: h1
                text: Places
                align in the top left
                font size: 30px
            contains multiple “Places” as listing (horizontal or vertical) describe by:
                tag: article
                width: 390px
                padding and margin 20px
                border #FF5A5F 1px with radius 4px
                contains the place name:
                    tag: h2
                    font size: 30px
                    center horizontally
    Requirements:

        You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 5 CSS files:
            styles/4-common.css: for the global style (i.e. body and .container styles)
            styles/3-header.css: for the header style
            styles/3-footer.css: for footer style
            styles/6-filters.css: for the filters style
            styles/7-places.css: for the places style
![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/bca4d17fbe21a58b66a9d5d6b85df4801d147dd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bb61c0dc51dcedc6861ac6b024baa44c38cacac19c7fa1889eb7b6a9ff876c0c)

8. More details

    Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

    Layout: (based on 7-index.html)

    Add more information to a Place article:

        Price by night:
            tag: div
            classname: price_by_night
            same level as the place name
            font color: #FF5A5F
            border: #FF5A5F 4px rounded
            min width: 60px
            height: 60px
            font size: 30px
            align: the top right (with space)
        Information section:
            tag: div
            classname: information
            height: 80px
            border: top and bottom #DDDDDD 1px
            contains (align vertically):
                Number of guests:
                    tag: div
                    classname: max_guest
                    width: 100px
                    fake text
                    icon
                Number of bedrooms:
                    tag: div
                    classname: number_rooms
                    width: 100px
                    fake text
                    icon
                Number of bathrooms:
                    tag: div
                    classname: number_bathrooms
                    width: 100px
                    fake text
                    icon
        User section:
            tag: div
            classname: user
            text Owner: <fake text>
            Owner text should be in bold
        Description section:
            tag: div
            classname: description
    Requirements:

        You must use: header, footer, section, article, button, h1, h2, h3, h4, ul, li tags
        No inline style
        You are not allowed to use the img tag
        You are not allowed to use the style tag in the head tag
        All images must be stored in the images folder
        You must have 5 CSS files:
            styles/4-common.css: for the global style (i.e. body and .container styles)
            styles/3-header.css: for the header style
            styles/3-footer.css: for the footer style
            styles/6-filters.css: for the filters style
            styles/8-places.css: for the places style
![image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f4b2d4ef94bd3a2e7e1ddefa81236595686d270e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20221202%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20221202T184950Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4a76430d73455f6758df51b335c9d57febc6455f2909760d5e6cdb13c38548ea)
