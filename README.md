# <div align='center'>NGL Send Message</div>
<div align='center'>

<p align="center">
  <img src="https://img.shields.io/badge/NGL-Library-blue?style=for-the-badge&logo=node.js" alt="Node Js" />
  <img src="https://img.shields.io/badge/version-1.0.0-green?style=for-the-badge" alt="Version 1.0.0" />
  <img src="https://img.shields.io/badge/license-GPL_v3-yellow?style=for-the-badge" alt="License GPL v3" />
</p>

<div align="center">
![logo](https://example.com/image.jpg)
</div>
![logo](https://example.com/image.jpg)

---

📖 About NGL

<div style="background: #f5f5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #007acc;">
<strong>NGL</strong> is an anonymous messaging app. You share a link often on Instagram or other social platforms and people can send you questions or messages without revealing their identity. Those messages then appear inside the strong>NGL</strong> app for you to read.
</div>

<br>

With this library, you can send anonymous messages to NGL users through programs you create.

---

🚀 Features

· Send anonymous messages to NGL accounts
· Supports TypeScript and CommonJS
· Easy to use 

---

📦 How to install

```bash
npm install @reyhan6610/ngl
```

```bash
yarn add @reyhan6610/ngl
```

---

💻 How To Use

CommonJS

```javascript
const { ngl } = require('@reyhan6610/ngl');

async function sendNGLMessage() {
  try {
    const result = await ngl[0].run({
      req: {
        query: {
          link: "https://ngl.link/target", //Your target
          text: "Hello!", //Message
          count: 5 //count message send max 1000
        }
      }
    });
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}

sendNGLMessage();
```

TypeScript

```typescript
import { ngl, ApiResponse } from '@reyhan6610/ngl';

async function testNGL(): Promise<void> {
  try {
    const result: ApiResponse = await ngl[0].run({
      req: {
        query: {
          link: "https://ngl.link/target", //Your target
          text: "Hello!", //Message
          count: "5" //count message send max 1000
        }
      }
    });
    
    console.log(JSON.stringify(result, null, 2));
    
    if (result.status) {
      console.log('Success:', result.data);
    } else {
      console.log(result.error);
    }
  } catch (error: any) {
    console.error(error.message);
  }
}

testNGL();
```

---

📋 Response

The library returns an object with the following structure: 

```json
{
  status: true,
  data: {
    totalAttempts: 5,
    successful: 5,
    failed: 0,
    results: [ [Object], [Object], [Object], [Object], [Object] ],
    errors: []
  },
  timestamp: '2025-11-16T06:45:02.087Z'
}
```
⚠️ Disclaimer

<div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107;">
<strong>Attention:</strong> Use this library wisely and responsibly. Unethical use or spam may violate NGL’s terms of service.
</div>🔧 Development

Want to contribute? Please fork this repository and create a pull request.

📄 License

GPL v3 License – see the LICENSE file for full details.
