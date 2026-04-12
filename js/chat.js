$(function () {
  "use strict";

  /* ============================================================
     CONSTANTS & STATE
     ============================================================ */

  // Mock AI responses with varied content including markdown
  const AI_RESPONSES = [
    "Great question! Here's a quick overview:\n\n**CSS Flexbox** is a one-dimensional layout method for arranging items in rows or columns. It gives you control over alignment, direction, order, and size of items.\n\nHere's a simple example:\n```css\n.container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  gap: 16px;\n}\n```\nItems inside `.container` will now be centered both horizontally and vertically.",
    "Sure! A common JavaScript pattern for reversing a string:\n\n```javascript\nfunction reverseString(str) {\n  return str.split('').reverse().join('');\n}\n\nconsole.log(reverseString('hello')); // 'olleh'\n```\n\nYou can also use the spread operator:\n```javascript\nconst reversed = [...str].reverse().join('');\n```",
    "**Async/Await vs Promises** — both handle asynchronous code, but async/await makes it *read* like synchronous code.\n\n```javascript\n// Promise approach\nfetch('/api/data')\n  .then(res => res.json())\n  .then(data => console.log(data))\n  .catch(err => console.error(err));\n\n// Async/Await approach\nasync function getData() {\n  try {\n    const res = await fetch('/api/data');\n    const data = await res.json();\n    console.log(data);\n  } catch (err) {\n    console.error(err);\n  }\n}\n```\nAsync/await is generally easier to read and debug, especially with multiple sequential calls.",
    "That's a fascinating topic! Here are some key **mobile UX principles**:\n\n- **Thumb-friendly design** — Keep interactive elements within easy reach\n- **Minimal input** — Reduce typing with smart defaults and autocomplete\n- **Progressive disclosure** — Show only what's needed at each step\n- **Fast loading** — Optimize assets and use skeleton screens\n- **Clear feedback** — Every action should have a visible response\n\nFollowing these guidelines helps create intuitive, enjoyable mobile experiences.",
    "I can help with that! Bootstrap 5's grid system is based on a **12-column flexbox layout**.\n\n```html\n<div class=\"container\">\n  <div class=\"row\">\n    <div class=\"col-md-6\">Left</div>\n    <div class=\"col-md-6\">Right</div>\n  </div>\n</div>\n```\n\nKey classes:\n- `container` / `container-fluid` — wraps the grid\n- `row` — creates a horizontal group\n- `col-*` — defines column width (1–12)\n\nBreakpoints: `xs`, `sm`, `md`, `lg`, `xl`, `xxl`",
    "Absolutely! Here's how **CSS Custom Properties** (variables) work:\n\n```css\n:root {\n  --primary-color: #4f7cff;\n  --spacing-md: 16px;\n  --border-radius: 8px;\n}\n\n.button {\n  background: var(--primary-color);\n  padding: var(--spacing-md);\n  border-radius: var(--border-radius);\n}\n```\n\nThe beauty is you can update `--primary-color` once in `:root` and it cascades everywhere. Great for theming!",
    "I'm doing great, thanks for asking! I'm here and ready to help you with code, design questions, explanations, or anything else you need. What's on your mind?",
    "That's an interesting question. The short answer is: **it depends on your use case!**\n\nFor most modern projects:\n- Use **`const`** by default\n- Use **`let`** when you need to reassign\n- Avoid **`var`** — it has confusing scoping rules\n\nThis approach makes your code more predictable and easier to reason about.",
  ];

  let messageCount = 0;
  let isTyping = false;
  let isDarkMode = true; // Default dark mode

  /* UTILITY FUNCTIONS */


  function getCurrentTime() {
    return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  }
  function getRandomResponse() {
    return AI_RESPONSES[Math.floor(Math.random() * AI_RESPONSES.length)];
  }
  function formatMessage(text) {
    // Escape HTML first
    let escaped = text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    // Fenced code blocks (``` ... ```)
    escaped = escaped.replace(/```(\w*)\n([\s\S]*?)```/g, function (_, lang, code) {
      return `<pre><code>${code.trim()}</code></pre>`;
    });

    // Inline code
    escaped = escaped.replace(/`([^`]+)`/g, "<code>$1</code>");

    // Bold
    escaped = escaped.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

    // Italic
    escaped = escaped.replace(/\*(.+?)\*/g, "<em>$1</em>");

    // Bullet lists: lines starting with "- "
    escaped = escaped.replace(/(^|\n)- (.+)/g, "$1<li>$2</li>");
    escaped = escaped.replace(/(<li>[\s\S]+?<\/li>)/g, "<ul>$1</ul>");

    // Newlines → <br> (but not inside <pre>)
    escaped = escaped.replace(/\n(?!<)/g, "<br />");

    return escaped;
  }
  /**
   * Appends a new message bubble to the chat
   * @param {string} text  — message content
   * @param {string} sender — "user" | "ai"
   */
  function addMessage(text, sender) {
    const isUser = sender === "user";
    const time = getCurrentTime();
    const formattedText = formatMessage(text);

    const avatarHtml = isUser
      ? `<div class="message-avatar user-avatar-msg">S</div>`
      : `<div class="message-avatar ai-avatar"><i class="fa-solid fa-bolt"></i></div>`;

    const messageHtml = `
      <div class="message ${isUser ? "user-message" : "ai-message"}">
        ${avatarHtml}
        <div class="message-bubble-wrap">
          <div class="message-meta">
            <span class="message-name">${isUser ? "You" : "AuraChat"}</span>
            <span class="message-time">${time}</span>
          </div>
          <div class="message-bubble">${formattedText}</div>
        </div>
      </div>`;

    $("#messages-wrapper").append(messageHtml);
    scrollToBottom();
    messageCount++;
  }

  function scrollToBottom() {
    const container = document.getElementById("messages-container");
    container.scrollTo({ top: container.scrollHeight, behavior: "smooth" });
  }

  /* ============================================================
     TYPING INDICATOR
     ============================================================ */

  function showTypingIndicator() {
    $("#typing-indicator").removeClass("hidden");
    scrollToBottom();
    isTyping = true;
  }

  function hideTypingIndicator() {
    $("#typing-indicator").addClass("hidden");
    isTyping = false;
  }
  function sendMessage() {
    const input = $("#message-input");
    const text = input.val().trim();

    if (!text || isTyping) return;

    // Hide welcome screen on first message
    if (messageCount === 0) {
      $("#welcome-screen").fadeOut(300, function () {
        $(this).remove();
      });
    }

    // Add user message
    addMessage(text, "user");

    // Clear & resize input
    input.val("").trigger("input");
    $("#send-btn").prop("disabled", true);

    // Show typing indicator, then respond after random delay
    showTypingIndicator();

    const delay = 1000 + Math.random() * 1000; // 1–2s
    setTimeout(function () {
      hideTypingIndicator();
      const response = getRandomResponse();

      if (window.typewriterEnabled) {
        // Typewriter effect (bonus feature)
        addMessageTypewriter(response, "ai");
      } else {
        addMessage(response, "ai");
      }
    }, delay);
  }
  function addMessageTypewriter(text, sender) {
    const time = getCurrentTime();
    const id = "tw-" + Date.now();

    const avatarHtml = `<div class="message-avatar ai-avatar"><i class="fa-solid fa-bolt"></i></div>`;

    const messageHtml = `
      <div class="message ai-message">
        ${avatarHtml}
        <div class="message-bubble-wrap">
          <div class="message-meta">
            <span class="message-name">AuraChat</span>
            <span class="message-time">${time}</span>
          </div>
          <div class="message-bubble" id="${id}"></div>
        </div>
      </div>`;

    $("#messages-wrapper").append(messageHtml);
    scrollToBottom();
    messageCount++;

    // Type out characters with slight delay
    const bubble = document.getElementById(id);
    let i = 0;

    function typeChar() {
      if (i < text.length) {
        bubble.textContent += text.charAt(i);
        i++;
        scrollToBottom();
        setTimeout(typeChar, 18);
      } else {
        // When done, apply full formatting
        bubble.innerHTML = formatMessage(text);
        scrollToBottom();
      }
    }
    typeChar();
  }
  $("#message-input").on("input", function () {
    this.style.height = "auto";
    this.style.height = Math.min(this.scrollHeight, 160) + "px";

    // Toggle send button
    const hasText = $(this).val().trim().length > 0;
    $("#send-btn").prop("disabled", !hasText);
  });

  // Enter = send, Shift+Enter = new line
  $("#message-input").on("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      if (!$(this).val().trim()) return;
      sendMessage();
    }
  });

  // Send button click
  $("#send-btn").on("click", sendMessage);

  // Suggestion cards — fill input and send
  $(document).on("click", ".suggestion-card", function () {
    const prompt = $(this).data("prompt");
    if (!prompt) return;
    $("#message-input").val(prompt).trigger("input").focus();
    setTimeout(sendMessage, 150);
  });

  var sidebarOpen = false;

  function openSidebar() {
    sidebarOpen = true;
    document.getElementById("sidebar").classList.add("open");
    document.getElementById("sidebar-overlay").classList.add("active");
    document.body.style.overflow = "hidden";
  }

  function closeSidebar() {
    sidebarOpen = false;
    document.getElementById("sidebar").classList.remove("open");
    document.getElementById("sidebar-overlay").classList.remove("active");
    document.body.style.overflow = "";
  }

  // Hamburger button — pure vanilla JS, no jQuery event issues
  document.getElementById("hamburger").addEventListener("click", function(e) {
    e.preventDefault();
    e.stopPropagation();
    if (sidebarOpen) {
      closeSidebar();
    } else {
      openSidebar();
    }
  });

  // Overlay click closes sidebar
  document.getElementById("sidebar-overlay").addEventListener("click", function() {
    closeSidebar();
  });

  // ESC key closes sidebar
  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape" && sidebarOpen) closeSidebar();
  });

  // Sidebar history items — visual active state
  $(document).on("click", ".history-item", function () {
    $(".history-item").removeClass("active");
    $(this).addClass("active");
    if (window.innerWidth <= 768) closeSidebar();
  });

  // New Chat button
  $("#new-chat-btn").on("click", function () {
    if (messageCount === 0) return;

    if (confirm("Start a new chat? This will clear the current conversation.")) {
      // Preserve the old chat in history (first 30 chars of last message)
      const lastMsg = $(".user-message .message-bubble").last().text().slice(0, 30);
      if (lastMsg) {
        const historyItem = `
          <div class="history-item">
            <i class="fa-regular fa-message"></i>
            <span>${lastMsg}…</span>
          </div>`;
        $(".history-item.active").removeClass("active");
        $(historyItem).prependTo("#chat-history").first().addClass("active");
      }

      // Reset chat
      $("#messages-wrapper").empty();
      messageCount = 0;
      isTyping = false;
      hideTypingIndicator();

      // Re-insert welcome screen
      const welcomeHtml = `
        <div id="welcome-screen" class="welcome-screen">
          <div class="welcome-logo">
            <span class="logo-glow"><i class="fa-solid fa-bolt"></i></span>
          </div>
          <h1 class="welcome-title">Hello, I'm AuraChat</h1>
          <p class="welcome-subtitle">Your intelligent AI companion. What would you like to explore today?</p>
          <div class="suggestion-grid">
            <div class="suggestion-card" data-prompt="Explain how CSS Flexbox works with examples">
              <div class="card-icon"><i class="fa-brands fa-css3-alt"></i></div>
              <div class="card-body-text">
                <div class="card-title">CSS Flexbox Guide</div>
                <div class="card-desc">Learn layouts with practical examples</div>
              </div>
            </div>
            <div class="suggestion-card" data-prompt="Write a JavaScript function to reverse a string">
              <div class="card-icon"><i class="fa-brands fa-js"></i></div>
              <div class="card-body-text">
                <div class="card-title">JavaScript Snippets</div>
                <div class="card-desc">Handy code patterns and functions</div>
              </div>
            </div>
            <div class="suggestion-card" data-prompt="What are the best UX design principles for mobile apps?">
              <div class="card-icon"><i class="fa-solid fa-mobile-screen"></i></div>
              <div class="card-body-text">
                <div class="card-title">Mobile UX Principles</div>
                <div class="card-desc">Design better mobile experiences</div>
              </div>
            </div>
            <div class="suggestion-card" data-prompt="Explain the difference between async/await and Promises in JavaScript">
              <div class="card-icon"><i class="fa-solid fa-code-branch"></i></div>
              <div class="card-body-text">
                <div class="card-title">Async JavaScript</div>
                <div class="card-desc">Promises vs async/await explained</div>
              </div>
            </div>
          </div>
        </div>`;

      $("#messages-container").prepend(welcomeHtml);
      if (window.innerWidth <= 768) closeSidebar();
    }
  });

  $("#theme-toggle").on("click", function () {
    isDarkMode = !isDarkMode;
    $("html").attr("data-theme", isDarkMode ? "" : "light");

    if (isDarkMode) {
      $("#theme-icon").removeClass("fa-sun").addClass("fa-moon");
      $("#theme-label").text("Dark Mode");
    } else {
      $("#theme-icon").removeClass("fa-moon").addClass("fa-sun");
      $("#theme-label").text("Light Mode");
    }
  });

  $("#export-btn").on("click", function () {
    if (messageCount === 0) {
      alert("No messages to export yet! Send a message first.");
      return;
    }

    let exportText = "AuraChat Export\n";
    exportText += "Generated: " + new Date().toLocaleString() + "\n";
    exportText += "=".repeat(50) + "\n\n";

    $(".message").each(function () {
      const name = $(this).find(".message-name").text();
      const time = $(this).find(".message-time").text();
      const content = $(this).find(".message-bubble").text();
      exportText += `[${time}] ${name}:\n${content}\n\n`;
    });

    // Use Blob API to trigger download
    const blob = new Blob([exportText], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "AuraChat_export_" + Date.now() + ".txt";
    a.click();
    URL.revokeObjectURL(url);
  });
  window.typewriterEnabled = false; // Set true to enable letter-by-letter effect
  // Focus input on load
  $("#message-input").focus();

  console.log("✅ AuraChat initialized successfully.");
});
