const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

(async () => {
  const url = process.argv[2];
  const file_path = process.argv[3];

  const browser = await puppeteer.launch();
  const page = (await browser.pages())[0];
  await page.goto(url);

  const html = await page.content();
  
  const file = path.join(file_path, 'dom.html');

  fs.writeFile(file, html, (err) => {
    if (err) throw err;
  });

  await browser.close();
})();
