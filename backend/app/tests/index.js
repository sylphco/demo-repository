const activeUsers = new Set();


const sio = io('http://localhost:8000');

sio.on('connect', () => {
	console.log('connected');
});

sio.on('disconnect', () => {
	console.log('disconnected');
});
