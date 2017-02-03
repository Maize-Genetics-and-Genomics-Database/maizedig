<?php
/* file: create_tagged_image.php
 *
 * purpose: main controller for tagged images pages
 *
 * history:
 *  06/24/16 jportwood created
 */


  //$img_name = $_GET['imgName'];
  $tag_id = $_GET['tagID'];
 // $tag_name = $_GET['tagName'];
  
  $log_file = "log/log.txt";
  
  $connect_str = 'host=localhost';
  $connect_str .= ' dbname=chado';
  $connect_str .= ' user=ktcho';
  $connect_str .= ' password=dev_chadodb';
  $DBConn = pg_connect($connect_str);

  
  $log = file_get_contents($log_file);
 
  if (!$log) $log = "";
  log_message("New link received for tag id $tag_id");
  
  /**TEST **/
 
 
  
  /** END TEST **/
  
  $img_info = getImgInfo($DBConn, $tag_id);
  //echo "<pre>"; var_dump($img_info); echo "</pre>";
  $tags = getAllTags($DBConn, $img_info["picture_id"]);
  //echo "<pre>"; var_dump($tags); echo "</pre>";
  $html_body = create_img_map($DBConn, $tags, $img_info);
  $html_body .= create_genelink_list($DBConn, $tags);
  //$coord_str = getTagCoords($DBConn, $tag_id, $factor);
  //$color_str = getColor($DBConn, $tag_id);
  /*TODO: Need to draw ALL of the tags that are on this image, not just the one passed as the GET parameter*/
 
  
  //$img_name = getImgName($DBConn, $tag_id);
  
  
  //echo "<br> coord_str: $coord_str";
  //echo "<br> color_str: $color_str";
  
  $headers = file_get_contents("main.html");
  /*$body = "<img src='http://biodig.maizegdb.org/media/pictures/$img_name' class='map' style='width: " . $new_size['width'] . "; height: " . $new_size['height'] . ";' usemap='#imgMap'/>
           <map name='imgMap'>
             <area id='$tag_name' shape='poly' coords='$coord_str' href='http://www.maizegdb.org/gbrowse/maize_v3test/?q=$tag_name' alt='$tag_name' title='Tag: $tag_name'
                    data-maphilight='{\"strokeColor\":\"222222\",\"strokeWidth\":1,\"fillColor\":\"$color_str\",\"fillOpacity\":0.6,\"alwaysOn\":true}'>
            </map>";
            */
     //TODO ADD MORE AREAS TO BODY//
  $html = str_replace("$(body)", $html_body, $headers);
  $log .= "\n";
  //file_put_contents("tags/$tag_name.html", $html);
  echo $html;
  file_put_contents($log_file, $log);
  
  //DONE?
  /*
    <img src="http://biodig.maizegdb.org/media/pictures/1465533209.33c38cb0573e60b3e4083598d039b46c4.png" class="map" style="width: 560px; height: 316px;" usemap="#simpleTest"/>
   <map name="simpleTest">
     <area id="wtf1" shape="poly" coords="431,54,431,55,431,56,431,59,431,60,431,61,431,62,431,63,431,64,431,65,431,66,431,67,431,68,431,69,431,70,431,71,431,72,431,73,431,74,432,74,432,75,432,76,433,76,433,77,433,78,433,79,433,80,433,81,433,82,433,83,433,84,433,85,433,86,433,87,433,88,433,89,434,90,434,91,435,91,436,91,437,91,439,91,440,91,441,91,442,91,443,91,444,91,445,91,446,91,447,91,448,91,449,91,450,91,451,91,451,90,452,90,453,90,454,90,455,90,456,90,457,90,458,90,459,90,460,90,461,90,462,90,463,90,464,90,465,90,466,90,466,91,467,91,467,92,468,92,468,93,469,93,470,93,471,93,472,93,473,93,474,93,475,93,476,93,476,92,476,91,476,90,477,90,477,89,477,88,477,87,477,86,477,85,477,84,477,83,476,83,476,82,475,81,475,80,475,79,475,78,475,77,475,76,474,76,474,75,474,74,473,74,473,73,473,72,473,71,472,70,472,69,471,69,471,68,471,67,471,66,471,65,471,64,471,63,471,62,471,61,471,60,471,59,471,58,471,57,471,56,471,55,471,54,471,53,471,52,471,51,471,50,471,49,471,48,471,47,470,46,468,45,468,44,467,44,466,44,466,43,465,43,464,43,463,43,462,43,461,43,460,43,459,43,458,43,457,43,456,43,455,43,454,43,453,43,452,43,452,44,451,44,450,44,449,44,448,44,447,44,446,45,446,46,445,46,445,47,444,47,443,48,443,49,442,49,441,49,440,49,439,49,439,50,438,50,437,50,436,50,435,50,434,50,434,50" href="sun.html" alt="wtf1 tag" title="wtf1 title"
     data-maphilight='{"strokeColor":"0000ff","strokeWidth":5,"fillColor":"ff0000","fillOpacity":0.6,"alwaysOn":true}'>
     <area id="wtf2" shape="square" coords="331,54,377,83" href="sun.html" alt="wtf2 tag" title="wtf2 title" data-maphilight='{"strokeColor":"00ff00","strokeWidth":5,"fillColor":"ff0000","fillOpacity":0.6}'>
     */
  
  
  function getTagCoords($DBConn, $tag_id, $factor) {
     $tag_query = "SELECT * 
                FROM public.tagpoint
                WHERE tag_id = $tag_id
                ORDER BY rank";
     $stmt = pg_prepare($DBConn, '', $tag_query);
     if ($stmt) {
       $stmt = pg_execute($DBConn, '', array());
     }
     $rows = pg_fetch_all($stmt);
     $coords = array();
     foreach ($rows as $row) {
       $coords['vals'] .= round($factor * $row['pointX']) . "," . round($factor * $row['pointY']) . ","; //keys may need to be all lower case
     }
     $coords['shape'] = (count($rows) == 2) ? "rect" : "poly";
     rtrim($coords['vals'], ",");
     return $coords;
  }
  
  function getColor($DBConn, $color_id) {
    /* $color_id_query = "SELECT color_id 
                     FROM public.tag
                     WHERE id = $tag_id";
     $stmt = pg_prepare($DBConn, '', $color_id_query);
     if ($stmt) {
       $stmt = pg_execute($DBConn, '', array());
     }
     $row = pg_fetch_assoc($stmt);
     //echo "<br>color_id: $color_id";
     */
     $color_query = "
                    SELECT red, green, blue
                    FROM public.tagcolor
                    WHERE id = " . $color_id;

     $stmt = pg_prepare($DBConn, '', $color_query);
     if ($stmt) {
       $stmt = pg_execute($DBConn, '', array());
     }
     $colors = pg_fetch_assoc($stmt);
     return sprintf("%02x", $colors["red"]) . sprintf("%02x", $colors["green"]) . sprintf("%02x", $colors["blue"]);
     //return dechex($colors["red"]) . dechex($colors["green"]) . dechex($colors["blue"]);
  }
  
  /**
   * Retrieve image info from database based on provided tag_id, and then find the width, height, and scaling factor of the image.
   * The scaling factor is used to adjust the tag coordinates since BioDIG scales the image to a MAX width/height when the tags 
   * are created
   **/
  function getImgInfo($DBConn, $tag_id) {
     $img_info_query = "
                      SELECT p.\"imageName\", p.id as picture_id
                      FROM public.tag t 
                      INNER JOIN public.taggroup tg on tg.id = t.group_id 
                      INNER JOIN public.picture p on p.id = tg.picture_id 
                      WHERE t.id = $tag_id;
                      ";
     $stmt = pg_prepare($DBConn, '', $img_info_query);
     if ($stmt) {
       $stmt = pg_execute($DBConn, '', array());
     }
     $img_info = pg_fetch_assoc($stmt);
     
     $MAX_WIDTH = 560; 
     $MAX_HEIGHT = 500;
     $img_path = "/var/www/BioDIG/taxon_home/media/". $img_info['imageName']; //TODO - Can this path change?
     $size = getimagesize($img_path);
     if (!$size) {
       log_message("Error could not open image: $img_path");
     }
     $img_info['width'] = $size[0];
     $img_info['height'] = $size[1];
     if ($img_info['width'] > $img_info['height']) {
       $img_info['factor'] = $img_info['width'] / $MAX_WIDTH;
     }
     else {
       $img_info['factor'] = $img_info['height'] / $MAX_HEIGHT;
     }
     return $img_info;
  }
  
  function getAllTags($DBConn, $picture_id) {
     $tag_query = "
                      SELECT t.id as tag_id, t.name as tag_name, t.color_id, tg.id as group_id 
                      FROM public.tag t 
                      INNER JOIN taggroup tg on tg.id = t.group_id 
                      WHERE tg.picture_id = $picture_id
                      ";
     $stmt = pg_prepare($DBConn, '', $tag_query);
     if ($stmt) {
       $stmt = pg_execute($DBConn, '', array());
     }
     $rows = pg_fetch_all($stmt);
     return $rows;
  }
  
  function create_img_map($DBConn, $tags, $img_info) {
    //style='width:".$img_info['width']."; height:".$img_info['height'].";'
    $html_body = "
          <img src='http://biodig.maizegdb.org/media/".$img_info["imageName"]."' class='map'  usemap='#imgMap'/>
          <map name='imgMap'>
          ";
    for ($i=0; $i<count($tags); $i++) {
        $coords = getTagCoords($DBConn, $tags[$i]['tag_id'], $img_info['factor']);
        $color_str = getColor($DBConn, $tags[$i]['color_id']);
        $html_body .= "       
             <area id='".$tags[$i]['tag_name']."_".$tags[$i]['tag_id']."' shape='".$coords['shape']."' coords='".$coords['vals']."'
                   href='#' alt='".$tags[$i]['tag_name']."' title='Tag: ".$tags[$i]['tag_name']."' class='tag'
                   data-maphilight='{\"strokeColor\":\"222222\",\"strokeWidth\":1,\"fillColor\":\"$color_str\",\"fillOpacity\":0.35,\"alwaysOn\":true}'>
                    ";
    }
    $html_body .= "</map>";
    return $html_body;
  }
  
  function create_genelink_list($DBConn, $tags) {
    //style='width:".$img_info['width']."; height:".$img_info['height'].";'
    $html = "";
    for ($i=0; $i<count($tags); $i++) {
        $gene_list = get_gene_list($DBConn, $tags[$i]['tag_id']);
        $html .= "<div id='".$tags[$i]['tag_name']."_".$tags[$i]['tag_id']."_genes' class='gene_list'>
                     <div class='gene_close'>
                       <span id='".$tags[$i]['tag_name']."_".$tags[$i]['tag_id']."_close' class='gene_close_text'>Close X</span>
                     </div>
                     <div class='gene_links'>
                       The following genes have been linked to this tag: <br>
                       $gene_list
                     </div>
                  </div>
                  ";
    }
    return $html;
  }
  
  function get_gene_list($DBConn, $tag_id) {
    $genelist_query = "
             SELECT f.name as gene_name
             FROM genelink g
             INNER JOIN feature f on g.feature_id = f.feature_id
             WHERE g.tag_id = $tag_id
             ";
    $stmt = pg_prepare($DBConn, '', $genelist_query);
    if ($stmt) {
      $stmt = pg_execute($DBConn, '', array());
    }
    $genes = pg_fetch_all($stmt);
    $gene_html = "";
    if (!$genes || count($genes) == 0) {
      log_message("Warning: No genes linked to tag id $tag_id");
      $gene_html .= "<i>None</i>";
    }
    else {
      foreach ($genes as $gene) {
        $gene_html .= "<a href='http://www.maizegdb.org/gene_center/gene/".$gene['gene_name']."/' target='_blank'>".$gene['gene_name']."</a>, ";
      }
      $gene_html = substr($gene_html, 0, -2);
    }
    
    return $gene_html;
  }
  
  function log_message($msg) {
    global $log;
    $log .=  date('Y-m-d g:i:sa') . " " . $msg . "\n";
  }
  /* Old
  function getImgName($DBConn, $tag_id) {
     $img_query = "
                      SELECT p.\"imageName\" 
                      FROM tag t 
                      INNER JOIN taggroup tg on tg.id = t.group_id 
                      INNER JOIN picture p on p.id = tg.picture_id 
                      WHERE t.id = $tag_id;
                      ";
     $stmt = pg_prepare($DBConn, '', $color_id_query);
     if ($stmt) {
       $stmt = pg_execute($DBConn, '', array());
     }
     $row = pg_fetch_assoc($stmt);
     return $row['imageName'];
  }
  */
  
  /**
   * Calculate new dimensions for image. The max sizes are determined when the biodig
   * img is zoomed out all of the way.
   *
   * TODO: Test this resizing funtion on MANY images of all shapes and sizes!!!
   */
   /*
  function getNewSize($img_path) {
    global $log;
    $MAX_WIDTH = 560; 
    $MAX_HEIGHT = 500;
    $new_size = array();
    $size = getimagesize($img_path);
    if (!$size) {
      $log .= date('Y-m-d g:i:sa') . " -- Error could not open image: $img_path\n";
    }
    $new_size['width'] = $size[0];
    $new_size['height'] = $size[1];
    if ($new_size['width'] >= $new_size['height'] && $new_size['width'] > $MAX_WIDTH) {
      //Resize width first, but maintain aspect ratio
      $factor = $MAX_WIDTH / $new_size['width'];
      $new_size['width'] = $MAX_WIDTH;
      $new_size['height'] = round($factor * $new_size['height']);
    }
    else if ($new_size['height'] > $MAX_HEIGHT) {
      //Resize height first
      $factor = $MAX_HEIGHT / $new_size['height'];
      $new_size['height'] = $MAX_HEIGHT;
      $new_size['width'] = round($factor * $new_size['width']);
    }
    return $new_size;
  }
  */
?>