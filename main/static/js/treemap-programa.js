
/*********************************/
/*** FUNCIONES DE AYUDA***/
/*********************************/


function reSortRoot(root,value_key) {
    //console.log("Calling");
    for (var key in root) {
     // console.log(key)
      if (key == "key") {
        root.name = root.key;
        delete root.key;
      }
      if (key == "values") {
        root.children = [];
        for (item in root.values) {
          root.children.push(reSortRoot(root.values[item],value_key));
        }
        delete root.values;
      }
      if (key == value_key) {
        root.value = parseFloat(root[value_key]);
        delete root[value_key];
      }
    }
    return root;
  }


/*********************************/
/*** FUNCION QUE HACE TODO EL TREEMAP ***/
/*********************************/

function Treemap2 (anio, presupuesto, idcanvas) {

/*********************************/
/*** CONFIGURACION DEL TREEMAP ***/
/*********************************/

var margin = {top: 20, right: 0, bottom: 0, left: 0},
    width = $(idcanvas).width(),
    height = 300 - margin.top - margin.bottom,
    formatNumber = d3.format(",d"),
    transitioning;

var x = d3.scale.linear()
    .domain([0, width])
    .range([0, width]);

var y = d3.scale.linear()
    .domain([0, height])
    .range([0, height]);

var treemap2 = d3.layout.treemap()
    .children(function(d, depth) { return depth ? null : d._children; })
    .sort(function(a, b) { return a.value - b.value; })
    .ratio(height / width * 0.5 * (1 + Math.sqrt(5)))
    .round(false);

var svg = d3.select(idcanvas).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.bottom + margin.top)
    .style("margin-left", -margin.left + "px")
    .style("margin.right", -margin.right + "px")
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
    .style("shape-rendering", "crispEdges");

var grandparent = svg.append("g")
    .attr("class", "grandparent");

grandparent.append("rect")
    .attr("y", -margin.top)
    .attr("width", width)
    .attr("height", margin.top);

grandparent.append("text")
    .attr("x", 6)
    .attr("y", 6 - margin.top)
    .attr("dy", ".75em");


/*********************************/
/*** traigo los datos y dibujo el treemap ***/
/*********************************/

d3.csv(presupuesto, function(csv_data) { // Traigo el csv


    historic_csv_data =  csv_data;

    /* csv_data = csv_data.filter(function (el) {
    return el.anho == anio;
    });*/
    // Add, remove or change the key values to change the hierarchy. 
    nested_data = d3.nest()
       // .key(function(d)  { return d.anho; })
        .key(function(d)  { return d.nivel1 ; })
        .key(function(d)  { return d.nivel2 ; })
        //.key(function(d)  { return d.nivel3; })
        .entries(csv_data);     

    console.log(nested_data);

    // Create the root node for the treemap
    var root = {};

    // Add the data to the tree
    root.key = "Gasto Total";
    root.values = nested_data;

    // Change the key names and children values from .next and add values for a chosen column to define the size of the blocks
    root = reSortRoot(root,"monto");

    console.log(root)


    initialize(root);
    accumulate(root);
    layout(root);  
    display(root);

  function initialize(root) {
    root.x = root.y = 0;
    root.dx = width;
    root.dy = height;
    root.depth = 0;
  }

  // Aggregate the values for internal nodes. This is normally done by the
  // treemap layout, but not here because of our custom implementation.
  // We also take a snapshot of the original children (_children) to avoid
  // the children being overwritten when when layout is computed.
  function accumulate(d) {
    return (d._children = d.children)
        ? d.value = d.children.reduce(function(p, v) { return p + accumulate(v); }, 0)
        : d.value;
  }

  // Compute the treemap layout recursively such that each group of siblings
  // uses the same size (1×1) rather than the dimensions of the parent cell.
  // This optimizes the layout for the current zoom state. Note that a wrapper
  // object is created for the parent node for each group of siblings so that
  // the parent’s dimensions are not discarded as we recurse. Since each group
  // of sibling was laid out in 1×1, we must rescale to fit using absolute
  // coordinates. This lets us use a viewport to zoom.
  function layout(d) {
    if (d._children) {
      treemap2.nodes({_children: d._children});
      d._children.forEach(function(c) {
        c.x = d.x + c.x * d.dx;
        c.y = d.y + c.y * d.dy;
        c.dx *= d.dx;
        c.dy *= d.dy;
        c.parent = d;
        layout(c);
      });
    }
  }



/* funcion que se llama display */
  function display(d) {
    grandparent
        .datum(d.parent)
        .on("click", transition)
      .select("text")
        .text(name(d));
    $(".treemap-datos").html("");

      sum = _.reduce(d._children, function(memo, num){ return memo + num.value; }, 0)

    $(".treemap-titulo").html(d.name);
    $(".treemap-monto").html("Gs. " + formatNumber(sum));

    console.log(d._children);
    d._children.reverse().map(function(d){

      if (d.name){         
     //   var name = d.name.slice(3);
      }
      else 
        {
          console.log(d);
      //    var name = d.subprograma.slice(3);
        }       
      $(".treemap-datos").append("<tr><td>" + name + "</td><td>"+ formatNumber(d.value) +"</td></tr>");        
    });


    prueba = historic_csv_data.filter(function (el) {

    return el.nivel1 ==  d.name ||  el.nivel2 ==  d.name //||  el.nivel ==  d.name;
    // return el.programa ==  d.name ||  el.subprograma ==  d.name ||  el.nivel ==  d.name;
    });



    prueba1 = d3.nest()
        .key(function(d)  { return d.nivel1; })
        .key(function(d)  { return d.nivel2; })
        .entries(prueba);
    prueba1 = reSortRoot(prueba1,"CAPITAL");

    console.log("prueba");
    console.log(prueba1);
    var g1 = svg.insert("g", ".grandparent")
        .datum(d)
        .attr("class", "depth");

    var g = g1.selectAll("g")
        .data(d._children)
      .enter().append("g");   


    g.filter(function(d) { return d._children; })
        .classed("children", true)
        .on("click", transition)
        .on("mouseover", function (d) { showPopover.call(this, d); })
        .on("mouseout", function (d) { removePopovers(); });
  
    g.selectAll(".child")
        .data(function(d) { return d._children || [d]; })
        .enter().append("rect")
        .attr("class", "child")
        .call(rect);
    var color = d3.scale.category10();
    g.append("rect")
        .attr("class", "parent")
        .style("fill", function(d) { ;return color(d.value); })
        .call(rect)
        .append("title")
        .text(function(d) { return 'Gs. '+  formatNumber(d.value); })
        ;


    g.append("text")
        .attr("dy", ".75em")
        .attr("fill", "rgb(51, 51, 51)")
        .text(function(d) {
          if (d.name) {
            texto_cortado =  d.name ;
          }         
          //texto = texto_cortado.split;
          if (texto_cortado.length >  25)
          {
            texto_cortado = texto_cortado.slice(0,25) + "...";
          }
          //  texto_cortado = texto_cortado.slice(3) + "...";
          return texto_cortado; 
        })         
        
        .attr("font-weight", "bold")
        .style("opacity", function(d) { return x(d.x + d.dx) - x(d.x) > 200 /*this.getComputedTextLength()  */? 1 : 0; })
        .call(text);

     g.append("text")
        .attr("dy", "1.85em")
        .text(function(d) { return 'Gs. '+  formatNumber(d.value); })
        .style("opacity", function(d) { return x(d.x + d.dx) - x(d.x) > 175 ? 1 : 0; })
        .call(text);



    function transition(d) {
      if (transitioning || !d) return;
      transitioning = true;
      //console.log(d._children);
      var g2 = display(d),
          t1 = g1.transition().duration(750),
          t2 = g2.transition().duration(750);

      // Update the domain only after entering new elements.
      x.domain([d.x, d.x + d.dx]);
      y.domain([d.y, d.y + d.dy]);

      // Enable anti-aliasing during the transition.
      svg.style("shape-rendering", null);

      // Draw child nodes on top of parent nodes.
      svg.selectAll(".depth").sort(function(a, b) { return a.depth - b.depth; });

      // Fade-in entering text.
      g2.selectAll("text").style("fill-opacity", 0);

      // Transition to the new view.
      t1.selectAll("text").call(text).style("fill-opacity", 0);
      t2.selectAll("text").call(text).style("fill-opacity", 1).style("opacity", function(d) { return x(d.x + d.dx) - x(d.x) > 200 /*this.getComputedTextLength()  */? 1 : 0; });
      t1.selectAll("rect").call(rect);
      t2.selectAll("rect").call(rect);

      // Remove the old node when the transition is finished.
      t1.remove().each("end", function() {
        svg.style("shape-rendering", "crispEdges");
        transitioning = false;
      });
    }//end transition

    return g;
  }// END DISPLAY

  function text(text) {
    text.attr("x", function(d) { return x(d.x) + 6; })
        .attr("y", function(d) { return y(d.y) + 6; });
  }

  function rect(rect) {
    rect.attr("x", function(d) { return x(d.x); })
        .attr("y", function(d) { return y(d.y); })
        .attr("width", function(d) { return x(d.x + d.dx) - x(d.x); })
        .attr("height", function(d) { return y(d.y + d.dy) - y(d.y); });
  }
  function name(d) {
    return d.parent
        ? name(d.parent) + " > " + d.name
        : d.name;
  }

   function removePopovers () {
          $('.popover').each(function() {
            $(this).remove();
          }); 
        }

  function showPopover (d) {
    $(this).popover({
      placement: 'auto top',
      container: 'body',
      trigger: 'manual',
      html : true,
      content: function() { 
      //  console.log(d);
        return "<h5>"+ d.parent.name+"</h5><hr><br/> <b> " + d.name + 
              "</b><br/><b>Monto:</b> Gs. " + formatNumber(d.value); ; 
      }
    });
    $(this).popover('show')
  }



});

}// End Treemap





