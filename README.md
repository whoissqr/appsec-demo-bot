## Hello,World!

<img src='https://qpluspicture.oss-cn-beijing.aliyuncs.com/6LjjQA/Hi.gif' alt='Hi' width="24"/> The following was actually forked from <a href="https://github.com/tw93/tw93/actions" target="_blank">tw93/actions</a> update every day；

<table>
<tr>
<td valign="top" width="50%">

#### 🏋️‍♀️ <a href="https://github.com/whoissqr/appsec-demo-bot/blob/master/releases.md" target="_blank">Product Releases</a>

<!-- recent_releases starts -->

<!-- recent_releases ends -->

</td>
<td valign="top" width="50%">

#### 🤹‍♀️ <a href="https://tw93.github.io/" target="_blank">Recent Blog</a>

<!-- blog starts -->

<!-- blog ends -->

</td>
</tr>
<tr>
<td valign="top" width="50%">

#### 🏊‍♂️ <a href="https://gist.github.com/whoissqr/45929d16ece946e3d25fb40c4878e112" target="_blank">Weekly Development Breakdown</a>

<!-- code_time starts -->

```text
Python             24 mins  █████████████████▓░░  73.4%
Markdown            8 mins  ████████░░░░░░░░░░░░  25.1%
JavaScript          0 secs  ███░░░░░░░░░░░░░░░░░   1.5%
```

<!-- code_time ends -->

</td>
<td valign="top" width="50%">

#### 🤾‍♂️ <a href="https://www.douban.com/people/kkshichao/" target="_blank">Funny Soul</a>

<!-- douban starts -->
* <a href='http://movie.douban.com/subject/1397546/' target='_blank'>想看追随</a> - 2020-06-14
* <a href='http://movie.douban.com/subject/30334073/' target='_blank'>想看调音师</a> - 2020-06-14
* <a href='http://movie.douban.com/subject/4072712/' target='_blank'>看过天涯同命鸟</a> - 2020-06-14
* <a href='http://movie.douban.com/subject/3077668/' target='_blank'>想看天水围的日与夜</a> - 2020-06-14
* <a href='http://movie.douban.com/subject/1306470/' target='_blank'>看过生死谍变</a> - 2020-02-28
<!-- douban ends -->

</td>
  </tr>
  </table>

<!-- fake commit 1 -->
<section id="blog" class="blog">
  <div class="blog__header">
    <p class="blog__header1">some of my</p>
    <h2 class="blog__header2">Medium
      <span class="blog__header2Span">posts</span>
    </h2>
  </div>
  <ul class="blog__slider">
    Posts go here
  </ul>
  <ul class="blog__counter">
    <li class="blog__counterItem blog__counterItem-active"></li>
    <li class="blog__counterItem"></li>
    <li class="blog__counterItem"></li>
  </ul>
</section>

a{
  color: inherit;
  text-decoration: none;
}
ul{
   list-style: none;
}

.blog{
   margin: 3rem 1rem;
   display: flex;
   flex-direction: column;
   justify-content: center;
   align-items: center;
   &__header{
      text-align: center;
   }
   &__header1{
      margin: 0;
      font-size: 1.1rem;
      font-weight: 300;
      letter-spacing: .2px;
      text-transform: uppercase;
   }
   &__header2{
      margin-top: .3rem;
      font-size: 1.4rem;
      font-weight: 500;
   }
   &__header2Span{
      font-weight: 400;
      font-size: 1.25rem;
   }
   &__slider{
      padding: 0;
      display: flex;
      flex-direction: row;
      justify-content: center
   }
   &__post{
      margin: 3rem 1rem;
      width: 25%;
      -webkit-box-shadow: 9px 9px 20px 0px rgba(0,0,0, .4);
      -moz-box-shadow: 9px 9px 20px 0px rgba(0,0,0, .4);
      box-shadow: 9px 9px 20px 0px rgba(0,0,0, .4);
   }
   &__topImg{
      max-width: 100%;
   }
   &__content{
      padding: .8rem;
   }
   &__preview{
      font-size: .95rem;
      font-weight: 300;
   }
   &__title{
      margin-top: 0;
      font-size: 1.4rem;
   }
   &__intro{
      line-height: 1.5;
   }
   &__info{
      font-weight: 300;
   }
   &__author{
      font-size: .9rem;
   }
   &__date{
      font-size: .85rem;
   }

   &__counter{
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: row;
   }
   &__counterItem{
      height: 20px;
      width: 20px;
      margin: .5rem;
      background-color: lightgray;
      border: 1px solid lightgray;
      border-radius: 25px;
      &:hover{
         cursor: pointer;
      }
   }
   &__counterItem-active{
      border: 1px solid lightblue;
      background-color: lightblue;
   }
}


