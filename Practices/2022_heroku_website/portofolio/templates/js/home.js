function copy_to_clip(text) {
    var dummy = document.createElement("input");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}


function dynamic_navbar(){
  const sections_ids = ["Portfolio-Card", "dynamic-resume", "dynamic-projects", "dynamic-blog", "dynamic-contact"];
  const navbar_elemnts = ["sec1", "sec2", "sec3", "sec4", "sec5"];
  for (i in [0,1,2,3,4]){
    // Check on each element on scroll events
    var section = document.getElementById(sections_ids[i]);
    var navbar_item = document.getElementById(navbar_elemnts[i]);
    // Get each section coordinates
    var bounding = section.getBoundingClientRect();
    // Check if partially visible
    if (bounding.top < window.innerHeight && bounding.bottom >= 0) {
      // If ture, remove all active from nav-bar items
      for (id of navbar_elemnts){
        var navbar_item_active = document.getElementById(id);
        navbar_item_active.classList.remove("active");
      }
      // And add active to the the true one (has the same index as the section)
      navbar_item.classList.add("active");
    }
  }
}


function switch_themes(status){
  // Light Mode => True
  // Dark Mode => False

  // Declare values
  if (status){
    var witched_color_headers = "black";
    var switched_color_normals = "black";
    var switched_color_navbar = "#49654e";
    var switched_color_background = "#efeee9";
    var switched_box_background = "rgba(255, 255, 255, .15)";
    var social_buttons = document.getElementsByTagName("button");
    var submit_button = document.getElementsByTagName("input");
    submit_button = submit_button[submit_button.length -1];
    var count = 0;
    for (button of social_buttons){
      count += 1;
      if (count == 1){
        continue;
      }
      if (count == 7){
        break;
      }
      button.classList.remove("button-hover-dark");
      submit_button.classList.remove("button-hover-dark");
      button.classList.add("button-hover-light");
      submit_button.classList.add("button-hover-light");
    }
  }else{
    var witched_color_headers = "white";
    var switched_color_normals = "rgb(255 255 255 / 75%)";
    var switched_color_navbar = "#212529";
    var switched_color_background = "#181d21";
    var switched_box_background = "#4a4a4a26";
    var social_buttons = document.getElementsByTagName("button");
    var submit_button = document.getElementsByTagName("input");
    submit_button = submit_button[submit_button.length -1];
    var count = 0;
    for (button of social_buttons){
      count += 1;
      if (count == 1){
        continue;
      }
      if (count == 7){
        break;
      }
      button.classList.remove("button-hover-light");
      submit_button.classList.remove("button-hover-light");
      button.classList.add("button-hover-dark");
      submit_button.classList.add("button-hover-dark");
    }
  }

  // Writings
  var headers = document.getElementsByClassName("switched-color-headers");
  var normals = document.getElementsByClassName("switched-color-normals");
  for (element of headers){
    element.style.color = witched_color_headers;
  }
  for (element of normals){
    element.style.color = switched_color_normals;
  }

  // Body background and navbar
  document.body.style.background = switched_color_background;
  var nav = document.getElementsByTagName("nav")[0]
  nav.style.background = switched_color_navbar;

  // Edit box and switch thumb
  var boxes = document.getElementsByClassName("box");
  var theme_switch = document.getElementsByClassName("toggle-thumb")[0];
  theme_switch.style.background = switched_color_navbar;
  for (element of boxes){
    element.style.background = switched_box_background;
  }
}