#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('Normal:');
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();

console.log('Empty Rectangle');
const r2 = new Rectangle(-1, -1);
r2.print();
r2.double();
r2.rotate();

