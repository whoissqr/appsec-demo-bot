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

<div class="code-wrap">
<pre id="css" class="code-box" aria-labeledby="css-editor-title">
              <code>
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
   &amp;__header{
      text-align: center;
   }
   &amp;__header1{
      margin: 0;
      font-size: 1.1rem;
      font-weight: 300;
      letter-spacing: .2px;
      text-transform: uppercase;
   }
   &amp;__header2{
      margin-top: .3rem;
      font-size: 1.4rem;
      font-weight: 500;
   }
   &amp;__header2Span{
      font-weight: 400;
      font-size: 1.25rem;
   }
   &amp;__slider{
      padding: 0;
      display: flex;
      flex-direction: row;
      justify-content: center
   }
   &amp;__post{
      margin: 3rem 1rem;
      width: 25%;
      -webkit-box-shadow: 9px 9px 20px 0px rgba(0,0,0, .4);
      -moz-box-shadow: 9px 9px 20px 0px rgba(0,0,0, .4);
      box-shadow: 9px 9px 20px 0px rgba(0,0,0, .4);
   }
   &amp;__topImg{
      max-width: 100%;
   }
   &amp;__content{
      padding: .8rem;
   }
   &amp;__preview{
      font-size: .95rem;
      font-weight: 300;
   }
   &amp;__title{
      margin-top: 0;
      font-size: 1.4rem;
   }
   &amp;__intro{
      line-height: 1.5;
   }
   &amp;__info{
      font-weight: 300;
   }
   &amp;__author{
      font-size: .9rem;
   }
   &amp;__date{
      font-size: .85rem;
   }

   &amp;__counter{
      margin: 0;
      padding: 0;
      display: flex;
      flex-direction: row;
   }
   &amp;__counterItem{
      height: 20px;
      width: 20px;
      margin: .5rem;
      background-color: lightgray;
      border: 1px solid lightgray;
      border-radius: 25px;
      &amp;:hover{
         cursor: pointer;
      }
   }
   &amp;__counterItem-active{
      border: 1px solid lightblue;
      background-color: lightblue;
   }
}

              </code>
            </pre>
            
<div class="code-wrap">
<pre id="js" class="code-box" aria-labeledby="js-editor-title">
              <code>
                fetch(&#39;https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@KonradDaWo&#39;)
   .then((res) =&gt; res.json())
   .then((data) =&gt; {
      // Filter for acctual posts. Comments don&#39;t have categories, therefore can filter for items with categories bigger than 0
      const res = data.items //This is an array with the content. No feed, no info about author etc..
      const posts = res.filter(item =&gt; item.categories.length &gt; 0) // That&#39;s the main trick* !

      // Functions to create a short text out of whole blog&#39;s content
      function toText(node) {
         let tag = document.createElement(&#39;div&#39;)
         tag.innerHTML = node
         node = tag.innerText
         return node
      }
      function shortenText(text,startingPoint ,maxLength) {
         return text.length &gt; maxLength?
         text.slice(startingPoint, maxLength):
         text
      }

      // Put things in right spots of markup
      let output = &#39;&#39;;
      posts.forEach((item) =&gt; {
         output += `
         &lt;li class=&quot;blog__post&quot;&gt;
            &lt;a href=&quot;${item.link}&quot;&gt;
               &lt;img src=&quot;${item.thumbnail}&quot; class=&quot;blog__topImg&quot;&gt;&lt;/img&gt;
               &lt;div class=&quot;blog__content&quot;&gt;
                  &lt;div class=&quot;blog_preview&quot;&gt;
                     &lt;h2 class=&quot;blog__title&quot;&gt;${shortenText(item.title, 0, 30)+ &#39;...&#39;}&lt;/h2&gt;
                     &lt;p class=&quot;blog__intro&quot;&gt;${&#39;...&#39; + shortenText(toText(item.content),60, 300)+ &#39;...&#39;}&lt;/p&gt;
                  &lt;/div&gt;
                  &lt;hr&gt;
                  &lt;div class=&quot;blog__info&quot;&gt;
                     &lt;span class=&quot;blog__author&quot;&gt;${item.author}&lt;/span&gt;
                     &lt;span class=&quot;blog__date&quot;&gt;${shortenText(item.pubDate,0 ,10)}&lt;/span&gt;
                  &lt;/div&gt;
               &lt;/div&gt;
            &lt;a/&gt;
         &lt;/li&gt;`

      })
      document.querySelector(&#39;.blog__slider&#39;).innerHTML = output
})


              </code>
            </pre>
