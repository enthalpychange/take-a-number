$(document).ready(function() {

  $(".incident-create").modalForm({
      formURL: "{% url 'incident-create' %}"
  });

});