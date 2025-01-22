class ChatManager {
    constructor(roomName, currentUsername) {
        this.roomName = roomName;
        this.currentUsername = currentUsername;
        this.chatSocket = null;
        this.messageInput = document.querySelector('#chat-message-input');
        this.chatForm = document.querySelector('#chat-form');
        this.chatMessages = document.querySelector('#chat-messages');
        
        this.initializeWebSocket();
        this.setupEventListeners();
        this.scrollToBottom();
    }

    initializeWebSocket() {
        this.chatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + this.roomName + '/'
        );

        this.chatSocket.onmessage = (e) => this.handleMessage(e);
        this.chatSocket.onclose = (e) => this.handleClose(e);
    }

    setupEventListeners() {
        this.chatForm.addEventListener('submit', (e) => this.handleSubmit(e));
        this.messageInput.addEventListener('keypress', (e) => this.handleKeyPress(e));
    }

    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    handleMessage(e) {
        const data = JSON.parse(e.data);
        const messageElement = document.createElement('div');
        const isCurrentUser = data.sender === this.currentUsername;
        
        messageElement.innerHTML = `
            <div class="flex ${isCurrentUser ? 'justify-end' : ''}">
                <div class="max-w-xs lg:max-w-md ${isCurrentUser ? 'bg-blue-500 text-white' : 'bg-white text-gray-800'} rounded-lg px-4 py-2 shadow">
                    <p class="text-sm">${data.message}</p>
                    <p class="text-xs mt-1 ${isCurrentUser ? 'text-blue-100' : 'text-gray-500'}">
                        ${new Date().toLocaleTimeString([], {hour: 'numeric', minute:'2-digit'})}
                    </p>
                </div>
            </div>
        `;
        
        this.chatMessages.appendChild(messageElement);
        this.scrollToBottom();
    }

    handleSubmit(e) {
        e.preventDefault();
        const message = this.messageInput.value.trim();
        if (message) {
            this.chatSocket.send(JSON.stringify({
                'message': message,
                'receiver_id': document.querySelector('#receiver-id').value
            }));
            this.messageInput.value = '';
        }
    }

    handleKeyPress(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            this.chatForm.dispatchEvent(new Event('submit'));
        }
    }

    handleClose(e) {
        console.error('Chat socket closed unexpectedly');
    }
}