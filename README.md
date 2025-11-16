@reyhan6610/ngl

<p align="center">
  <!-- Badge NGL dengan logo custom: ganti data:image/svg… dengan base64 SVG logo NGL kamu -->
  <img src="https://img.shields.io/badge/NGL-Library-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB…(base64 logo NGL)…" alt="NGL Library" />
  <img src="https://img.shields.io/badge/version-1.0.0-green?style=for-the-badge" alt="Version 1.0.0" />
  <img src="https://img.shields.io/badge/license-GPL_v3-yellow?style=for-the-badge" alt="License GPL v3" />
</p>

📖 Tentang NGL

<div style="background: #f5f5f5; padding: 15px; border-radius: 8px; border-left: 4px solid #007acc;">
<strong>NGL</strong> (Not Gonna Lie) adalah aplikasi dan layanan anonim untuk mengirimkan pertanyaan atau pesan tanpa menampilkan identitas pengirim. Biasanya digunakan bersama Instagram atau platform sosial lainnya.
</div>

<br>

Dengan library ini, Anda dapat mengirim pesan anonim ke pengguna NGL melalui program yang Anda buat.

🚀 Fitur

· ✅ Mengirim pesan anonim ke akun NGL
· ✅ Support TypeScript dan CommonJS
· ✅ Error handling yang baik
· ✅ Mudah digunakan

📦 Instalasi

```bash
npm install @reyhan6610/ngl
```

atau

```bash
yarn add @reyhan6610/ngl
```

💻 Cara Penggunaan

CommonJS

```javascript
const { ngl } = require('@reyhan6610/ngl');

async function sendNGLMessage() {
  try {
    const result = await ngl[0].run({
      req: {
        query: {
          link: "https://ngl.link/crypto92935",
          text: "Hello!",
          count: 5
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
          link: "https://ngl.link/crypto92935",
          text: "Hello!",
          count: "5"
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

⚙️ Parameter

<table style="width:100%; border-collapse: collapse;">
  <thead>
    <tr style="background-color: #007acc; color: white;">
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">Parameter</th>
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">Tipe</th>
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">Deskripsi</th>
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd;">Wajib</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 12px; border: 1px solid #ddd;"><code>link</code></td>
      <td style="padding: 12px; border: 1px solid #ddd;">string</td>
      <td style="padding: 12px; border: 1px solid #ddd;">Link NGL target</td>
      <td style="padding: 12px; border: 1px solid #ddd; text-align: center;">✅</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #ddd;"><code>text</code></td>
      <td style="padding: 12px; border: 1px solid #ddd;">string</td>
      <td style="padding: 12px; border: 1px solid #ddd;">Pesan yang akan dikirim</td>
      <td style="padding: 12px; border: 1px solid #ddd; text-align: center;">✅</td>
    </tr>
    <tr>
      <td style="padding: 12px; border: 1px solid #ddd;"><code>count</code></td>
      <td style="padding: 12px; border: 1px solid #ddd;">number | string</td>
      <td style="padding: 12px; border: 1px solid #ddd;">Jumlah pesan yang dikirim</td>
      <td style="padding: 12px; border: 1px solid #ddd; text-align: center;">✅</td>
    </tr>
  </tbody>
</table>

📋 Response

Library mengembalikan object dengan struktur berikut:

```typescript
interface ApiResponse {
  status: boolean;
  data?: any;
  error?: string;
}
```

⚠️ Catatan Penting

<div style="background: #fff3cd; padding: 15px; border-radius: 8px; border-left: 4px solid #ffc107;">
<strong>Perhatian:</strong> Gunakan library ini dengan bijak dan bertanggung jawab. Penggunaan yang tidak etis atau spam dapat melanggar ketentuan layanan NGL.
</div>

🔧 Development

Ingin berkontribusi? Silakan fork repository ini dan buat pull request!

📄 License

MIT License - lihat file LICENSE untuk detail lengkap.

---

<div align="center">
Dibuat dengan ❤️ oleh <a href="https://github.com/reyhan6610">reyhan6610</a>
</div>
