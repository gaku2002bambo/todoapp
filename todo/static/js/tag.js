document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');
 

  var calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    
    events: {
      url:'/api/events',
      method:'GET'
    }
    

    
  });
  calendar.render();
});