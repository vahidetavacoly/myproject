
let peer = new SimplePeer({ initiator: true, trickle: false });

peer.on('signal', data => {
    // ارسال سیگنال به دیگر طرف از طریق WebSocket
    socket.send(JSON.stringify({ type: 'offer', data: data }));
});

peer.on('stream', stream => {
    // پخش استریم ویدیو از طرف مقابل
    document.getElementById('remote-video').srcObject = stream;
});

// گرفتن سیگنال‌ها از WebSocket
socket.onmessage = function(event) {
    let data = JSON.parse(event.data);
    if (data.type === 'offer') {
        peer.signal(data.data);
    }
};