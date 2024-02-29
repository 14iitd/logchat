// Sample data for recent chats and messages
const recentChats = ['User1', 'User2', 'User3'];
const messages = [
    { sender: 'User1', content: 'Hello!', timestamp: '12:00 PM' },
    { sender: 'User2', content: 'Hi there!', timestamp: '12:05 PM' },
    // Add more messages as needed
];

// Function to initialize the UI
function initUI() {
    // Populate recent chats
    const recentChatsList = document.getElementById('recentChatsList');
    recentChats.forEach(chat => {
        const listItem = document.createElement('li');
        listItem.textContent = chat;
        listItem.onclick = () => openChat(chat);
        recentChatsList.appendChild(listItem);
    });

    // Display initial messages in the chat area
    displayMessages(messages);
}

// Function to open a 1-1 chat
function openChat(user) {
    document.querySelector('.chat-header h2').textContent = `1-1 Chat with ${user}`;
    // Simulate loading chat messages for the selected user (replace with actual data fetching)
    const userMessages = messages.filter(msg => msg.sender === user || msg.receiver === user);
    displayMessages(userMessages);
}

// Function to display messages in the chat area
function displayMessages(messages) {
    const chatMessages = document.getElementById('chatMessages');
    chatMessages.innerHTML = '';

    messages.forEach(msg => {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = `${msg.sender}: ${msg.content} (${msg.timestamp})`;
        chatMessages.appendChild(messageDiv);
    });
}

// Function to send a message (replace with actual message sending logic)
function sendMessage() {
    const inputField = document.getElementById('messageInput');
    const message = inputField.value;

    // Simulate sending the message (replace with actual sending logic)
    const newMessage = { sender: 'You', content: message, timestamp: getCurrentTime() };
    messages.push(newMessage);

    // Update the chat area with the new message
    displayMessages(messages);

    // Clear the input field
    inputField.value = '';
}

// Function to get the current time in HH:MM AM/PM format
function getCurrentTime() {
    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    const formattedHours = hours % 12 === 0 ? 12 : hours % 12;
    const formattedMinutes = minutes < 10 ? '0' + minutes : minutes;
    return `${formattedHours}:${formattedMinutes} ${ampm}`;
}

// Initialize the UI
initUI();
