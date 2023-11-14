args = process.argv.slice(2);

size = parseInt(args[0]);

if (!size)
    console.log('Missing size');

for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        process.stdout.write('x');
    }
    process.stdout.write('\n');
}
