<?php
/* Template Name: Alexa FB RSS Feed*/

header("Content-Type: application/rss+xml; charset=UTF-8");
echo '<?xml version="1.0"?>';
?>

<rss version="2.0"
xmlns:content="http://purl.org/rss/1.0/modules/content/"
xmlns:wfw="http://wellformedweb.org/CommentAPI/"
xmlns:dc="http://purl.org/dc/elements/1.1/"
xmlns:atom="http://www.w3.org/2005/Atom"
xmlns:sy="http://purl.org/rss/1.0/modules/syndication/"
xmlns:slash="http://purl.org/rss/1.0/modules/slash/"
<?php do_action('rss2_ns'); ?>
>

<channel>
<title><?php bloginfo_rss('name'); ?></title>
<link><?php bloginfo_rss('url') ?></link>
<atom:link href="<?php self_link(); ?>" rel="self" type="application/rss+xml" />
<description>Alexa FB Feed</description>
<lastBuildDate><?php echo mysql2date('D, d M Y H:i:s +0200', get_lastpostmodified('blog'), false); ?></lastBuildDate>
<language>de-DE</language>

<?php

/* Text-Laenge: */
function text($string, $length = '4500', $replacer = '...') {
  $string = preg_replace("/\[caption.*\[\/caption\]/", '', strip_tags($string));
  if(strlen($string) > $length)
    return (preg_match('/^(.*)\W.*$/', substr($string, 0, $length+1), $matches) ? $matches[1] : substr($string, 0, $length)) . $replacer;
  return $string;
}

$numposts = 10;
$posts = query_posts('showposts='.$numposts);
foreach ($posts as $post) {

?>

<item>
<title><?php echo get_the_title($post->ID); ?></title>
<link><?php echo get_permalink($post->ID); ?></link>
<pubDate><?php echo mysql2date('D, d M Y H:i:s +0000', get_post_time('Y-m-d H:i:s', true), false); ?></pubDate>
<description><?php echo text($post->post_content);  ?></description>
<dc:creator><?php echo the_author($post->ID); ?></dc:creator>
<guid><?php echo get_permalink($post->ID); ?></guid>
</item>

<?php } ?>

</channel>
</rss>
