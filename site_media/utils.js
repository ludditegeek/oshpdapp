
function findValue(li) {
	if( li == null ) return alert("No match!");

	// if coming from an AJAX call, let's use the CityId as the value
	if( !!li.extra ) var sValue = li.extra[0];

	// otherwise, let's just display the value in the text box
	else var sValue = li.selectValue;

	alert("The value you selected was: " + sValue);
}

function selectItem(li) {
	findValue(li);
}

function formatItem(row) {
	return row[0] + " (id: " + row[1] + ")";
}

function lookupAjax(){
	var oSuggest = $("#CityAjax")[0].autocompleter;

	oSuggest.findValue();

	return false;
}

function lookupLocal(){
	var oSuggest = $("#CityLocal")[0].autocompleter;

	oSuggest.findValue();

	return false;
}


function popform(){
	// set value in target 
	attr('id_icd9codedscr', 'testtesttest');
	}


$(document).ready(function () {

	// define various js fns to call here

	// Bind handler to result handler for code lookup
	$('input#id_icd9codedscr').result(function(event, data, formatted) {
	 	$("#result").html( !data ? "No match!" : "Selected: " + formatted);
	});

	//Change display based on selected value
	$("#id_codetype").change(onSelectChange);
		
	// make server call to retrieve matching ICD9 code list  + description
	// define ajax method in views.py & set up matching url to route this
	// server retrieves matching ICD9 code  + description (e.g. '411;dscr')
	// 4/20/10 - update to load selected value into a separate field (id_icd9codedscr)
	//           and strip off the description and leave just the code in the orig field
	$("#id_diagcodeicd9").autocomplete(
		'/ajax/icd9/autocomplete', {
			delay:400,
			minChars:2,
			max:20,
                        multiple:false,
			selectFirst: false,
			width: 600,
			formatItem: function(row){
				//split off code value
				var r1 = row[0];
				var rslt = r1.split(";");
 				var ret = '<span class="code">' + row[0] + '</span><br />';
				return ret;					
			},
			formatValue: function(row){
				var r1 = row[0];
				var rslt = r1.split(";");				
				return rslt[0];
				//return row['aaaa'];
			}
			//onItemSelect:popform
			//matchSubset:1,
			//matchContains:false
			//cacheLength:10,
			//onItemSelect:selectItem,
			//onFindValue:findValue,
			//formatItem:formatItem,
			//autoFill:true
		}).result(function(event,data,formatted) {
 			//$("input#id_icd9codedscr").html( !data ? "No match!" : "Selected: " + formatted);
			// set target value
			//$("#id_icd9codedscr").val('aaa');
			var s = data[0].split(";")
			//$("#id_icd9codedscr").val(data);
			$("#id_diagcodeicd9").val(s[0]);
			$("#id_icd9codedscr").val(s[1]);
	});	
});

function onSelectChange(){
	var selected = $("#id_codetype option:selected");
	//alert ('selection changed');		
	var output = "";
	if(selected.val() != 0){
		output = "You Selected " + selected.text();
	}
	if(selected.val() != 'DIAG'){
		// hide cpaa field
		//$("#id_diagcpaa").hide();
		//$('#dxtype').hide();
		$('.cpaa').hide();

	}
	else {
		//$('#dxtype').show();
		//$("#id_diagcpaa").show();
		$('.cpaa').show();

	}	
	$("#output").html(output);
}


