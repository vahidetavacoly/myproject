
document.addEventListener("DOMContentLoaded", function() {

    const userRole = '{{ user_role }}';  // اطمینان از اینکه user_role به درستی تعریف و ارسال شده است
    const appointmentId = '{{ appointment.id }}';  // اطمینان از اینکه appointment.id به درستی تعریف و ارسال شده است

    let socketURL = `ws://${window.location.host}/ws/chat/${userRole}/${appointmentId}/`;

    const chatSocket = new WebSocket(socketURL);

    chatSocket.onopen = function(e) {
        console.log('WebSocket connection established.');
    };

    chatSocket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        console.log('Received message:', data.message);
        // مدیریت پیام دریافت شده
    };

    chatSocket.onclose = function(e) {
        console.error('WebSocket connection closed unexpectedly.');
    };

    function sendMessage() {
        const message = document.getElementById(`${userRole}-message-input`).value;

        if (message && chatSocket.readyState === WebSocket.OPEN) {
            chatSocket.send(JSON.stringify({
                'message': message,
                'sender_id': '{{ user.id }}',  // فرض بر اینکه user.id به درستی ارسال شده است
                'role': userRole
            }));
            document.getElementById(`${userRole}-message-input`).value = '';
        }
    }
});

