
var goal = []
var goalIds = [];
function getGoal(id) {
  if (goal.length > 0) {
    var data = {
      id: id,
      content: $("#cont_" + id).text()
    }
    var x = JSON.stringify(data)
    var index = goal.indexOf(x)
    if (index == -1) {
      goal.push(x)
    } else {
      goal.splice(index, 1)
    }
  } else {
    var data = {
      id: id,
      content: $("#cont_" + id).text()
    }
    var x = JSON.stringify(data)
    goal.push(x)
  }
  localStorage.setItem("goal", JSON.stringify(goal))
  goalIds = goal.map(element => JSON.parse(element).id);
  console.log(goalIds)
  issample();
}

function issample() {
  $("#goal").val(goalIds);
  console.log(goalIds)
}
function initGoals() {
  var storedNames = JSON.parse(localStorage.getItem("goal") || '[]');
  goalIds = storedNames.map(element => JSON.parse(element).id);
}

$(function(){
let storedNames =JSON.parse(localStorage.getItem("goal") || '[]');
$.each(storedNames, function( index, value ) {
let temp = JSON.parse(value);
$('#room_'+temp['id']).addClass("blue");
console.log($('#'+temp['id']).attr('id'));
});
})