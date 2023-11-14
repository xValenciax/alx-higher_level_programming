#!/usr/bin/node

args = process.argv.slice(2);

if (!args)
    console.log(0);

else {
    let max = args[0];
    let sec_max = args[0];
    for (let arg of args) {
        if (arg > max)
        {
            sec_max = max;
            max = arg;
        }
    }
    console.log(sec_max);
}
