// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});


$(document).ready(function() {
  $('#dataTable-salary').DataTable({
        "order": [ 0, "desc" ],
    } );
});

$(document).ready(function() {
  $('#dataTable-salary-all').DataTable({
        "order": [ 0, "desc" ],
    } );
});

$(document).ready(function() {
  $('#dataTable-attendance').DataTable({
        "order": [ 0, "desc" ],
    } );
});