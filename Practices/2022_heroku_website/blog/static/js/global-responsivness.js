function switch_themes(obj){
	if (obj){
		// Light Mode => True
  		// Dark Mode => False

  		// Declare values
  		var witched_color_headers = "black";
	    var switched_color_normals = "black";
	    var hover_remove = "post-title-thumbnail-hover-dark";
	    var hover_add = "post-title-thumbnail-hover-light";
        var switched_color_background = "#efeee9";
	    var switched_box_background = "rgba(255, 255, 255, .15)";
	}else{
		var witched_color_headers = "white";
	    var switched_color_normals = "rgb(255 255 255 / 75%)";
	    var hover_remove = "post-title-thumbnail-hover-light";
	    var hover_add = "post-title-thumbnail-hover-dark";
	    var switched_color_background = "#181d21";
    	var switched_box_background = "#4a4a4a26";
	}

	// Edit background color and box color
	document.body.style.background = switched_color_background;
	var boxes = document.getElementsByClassName("box");
	var theme_switch = document.getElementsByClassName("toggle-thumb")[0];
	for (element of boxes){
	  element.style.background = switched_box_background;
	}

	// Edit page text
	var headers = document.getElementsByClassName("switched-color-headers");
  	var normals = document.getElementsByClassName("switched-color-normals");
  	var links = document.getElementsByClassName("post-title-thumbnail");
  	for (element of headers){
    	element.style.color = witched_color_headers;
	}
	for (element of normals){
		element.style.color = switched_color_normals;
	}
	for (element of links){
		element.style.color = witched_color_headers;
		element.classList.remove(hover_remove);
		element.classList.add(hover_add);
	}
}
