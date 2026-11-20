# Контрольная группа: геометрия слайда Iron Man при 1440x1024.
@objects
  slide        .slide
  left         .left-rail
  hero         .hero
  content      .content
  logo         .logo
  characters   .characters
  title        .story h1
  description  .story p
  image        .hero-image
  button       .buy
  footer       .slide-footer
  number       .number

= Основные области =
  slide:
    width 1440px
    height 1024px
  left:
    width 330px
    inside slide
  hero:
    width 500px
    height 1024px
    right-of left 0px
    inside slide
  content:
    width 610px
    right-of hero 0px
    inside slide

= Элементы макета =
  logo:
    inside slide 60px top, 50px left
    width 136px
  characters:
    inside slide 390px top, 50px left
  image:
    inside slide 140px top, 189px left
    width 729px
  title:
    inside slide 205px top, 866px left
    text matches "(?i)ironman"
  description:
    below title 25px
    text contains "Iron Man is a superhero"
  button:
    inside slide 669px top, 866px left
    width 171px
    height 57px
    text is "Buy Posters"
  footer:
    inside slide 841px top, 866px left
  number:
    text is "02"
