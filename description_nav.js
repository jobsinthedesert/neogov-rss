const path = require('path');
const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = (await browser.pages())[0];
  //command line argument: url
  await page.goto(process.argv[2]);

  const html = await page.content();
  
  url = await page.evaluate(() => {
    return document.querySelector('.print-button').getAttribute('href')
  })

  await page.goto(url);
  await page.content();

  //command line argument: file location
  await page.pdf({path: process.argv[3]});

  await browser.close();  
})();