// Generic search - reference different search functions based on caller URL
//

function search_submit() {
  var query = $("#id_query").val();
  
  var x =0;
  var uri = window.location;
  // fn call to parse uri - extract required component
  parseUri.options.strictMode = true;
  //var res = parseUri(uri).queryKey.query;
  var res = parseUri(uri).directory;
    
  // match on regexp
  //alert(uri);
  //alert(res);
  
  
  // conditional load based on source location - use regexp to parse??
  // link: http://stevenlevithan.com/demo/parseuri/js/
  
  //if (x > 0) {
  if (res =="/dxsearch/") {
	  $("#search-results").load(
	    "/dxsearch/?ajax&query=" + encodeURIComponent(query)
	  ); 
     }else{
	  $("#search-results").load(
	    "/prsearch/?ajax&query=" + encodeURIComponent(query)
	  );     
     }  // end if
     
  return false;	
}

$(document).ready(function () {

    var loc = window.location;
    //alert('got data');
    //alert(res);


  $("#search-form").submit(search_submit);
});


//}


//function search_submit() {
// get the query value
//  var query = $("#id_query").val();
//  
//  $("#search-results").load(
//    "/prsearch/?ajax&query=" + encodeURIComponent(query)
//  );
//  return false;
//}
//
//$(document).ready(function () {
//  $("#search-form").submit(search_submit);
//});


//

//
// try calling different search methods based on the form that is invoking the search
// call dx search or prescreen search conditionally
// in either case results are loaded into "search-results" div
// need to create url and view entries for these links
//
//
//  caller = windows.location()
//
//  if (caller == 'a') {
//  
//  $("#search-results").load(
//    "/dxsearch/?ajax&query=" + encodeURIComponent(query)
//  );
//  }else{
//  $("#search-results").load(
//    "/prsearch/?ajax&query=" + encodeURIComponent(query)
//  );
//  }
//  return false;
//}


//$(document).ready(function () {
//  $("#search-form").submit(search_submit);
//});
