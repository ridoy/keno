// Reads data dir, writes JSON mapping game # to array of numbers drawn (for concision)
// Note to future self. I don't know why I wrote this in a separate file in a separate language.
const fs= require('fs');
const gap = 20;
const dict = {};
const start = 2098753;
const end = 2163853;
for (let i = start; i<end+20;i+=20) {
    let file = fs.readFileSync(`${i}.txt`, 'utf-8');
    let draws = JSON.parse(file).result
    for (let draw of draws) {
        dict[draw.draw_number] = [
            draw.draw_num_1, 
            draw.draw_num_2, 
            draw.draw_num_3, 
            draw.draw_num_4, 
            draw.draw_num_5, 
            draw.draw_num_6, 
            draw.draw_num_7, 
            draw.draw_num_8, 
            draw.draw_num_9, 
            draw.draw_num_10,
            draw.draw_num_11,
            draw.draw_num_12,
            draw.draw_num_13,
            draw.draw_num_14,
            draw.draw_num_15,
            draw.draw_num_16,
            draw.draw_num_17,
            draw.draw_num_18,
            draw.draw_num_19,
            draw.draw_num_20
        ]
    }
}


fs.writeFileSync('hello.txt', JSON.stringify(dict), 'utf-8');
console.log('Done writing');
