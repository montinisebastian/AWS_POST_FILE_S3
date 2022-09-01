import React from 'react';

function CalcularHASH256_2(valorEntrada){
    var forge = require('node-forge');
    var input_str = valorEntrada;
    var md = forge.md.sha256.create();
    md.update(input_str);
    //console.log("Input String: "+ input_str);
    //console.log("Hash Value: " + md.digest().toHex());

    return md.digest().toHex();
        
}

        
export default CalcularHASH256_2;