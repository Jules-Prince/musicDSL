import type {Music,Note,Track, TrackSet, TimeSignature} from '../language/generated/ast.js';
import * as fs from 'node:fs';
import { CompositeGeneratorNode, toString } from 'langium';
import * as path from 'node:path';
import { extractDestinationAndName } from './cli-util.js';

const noteMap: { [key: string]: number } = {
    'C0': 12, 'C#0': 13, 'D0': 14, 'D#0': 15, 'E0': 16, 'F0': 17, 'F#0': 18, 'G0': 19, 'G#0': 20, 'A0': 21, 'A#0': 22, 'B0': 23,
    'C1': 24, 'C#1': 25, 'D1': 26, 'D#1': 27, 'E1': 28, 'F1': 29, 'F#1': 30, 'G1': 31, 'G#1': 32, 'A1': 33, 'A#1': 34, 'B1': 35,
    'C2': 36, 'C#2': 37, 'D2': 38, 'D#2': 39, 'E2': 40, 'F2': 41, 'F#2': 42, 'G2': 43, 'G#2': 44, 'A2': 45, 'A#2': 46, 'B2': 47,
    'C3': 48, 'C#3': 49, 'D3': 50, 'D#3': 51, 'E3': 52, 'F3': 53, 'F#3': 54, 'G3': 55, 'G#3': 56, 'A3': 57, 'A#3': 58, 'B3': 59,
    'C4': 60, 'C#4': 61, 'D4': 62, 'D#4': 63, 'E4': 64, 'F4': 65, 'F#4': 66, 'G4': 67, 'G#4': 68, 'A4': 69, 'A#4': 70, 'B4': 71,
    'C5': 72, 'C#5': 73, 'D5': 74, 'D#5': 75, 'E5': 76, 'F5': 77, 'F#5': 78, 'G5': 79, 'G#5': 80, 'A5': 81, 'A#5': 82, 'B5': 83,
    'C6': 84, 'C#6': 85, 'D6': 86, 'D#6': 87, 'E6': 88, 'F6': 89, 'F#6': 90, 'G6': 91, 'G#6': 92, 'A6': 93, 'A#6': 94, 'B6': 95,
    'C7': 96, 'C#7': 97, 'D7': 98, 'D#7': 99, 'E7': 100, 'F7': 101, 'F#7': 102, 'G7': 103, 'G#7': 104, 'A7': 105, 'A#7': 106, 'B7': 107,
    'C8': 108, 'C#8': 109, 'D8': 110, 'D#8': 111, 'E8': 112, 'F8': 113, 'F#8': 114, 'G8': 115, 'G#8': 116, 'A8': 117, 'A#8': 118, 'B8': 119,
    'C9': 120, 'C#9': 121, 'D9': 122, 'D#9': 123, 'E9': 124, 'F9': 125, 'F#9': 126, 'G9': 127
};

const drumMap: { [key: string]: number } = {
    'bd': 36,  // Kick Drum ou Bass Drum
    'sd': 38,  // Snare Drum
    'ch': 42,  // Closed Hi-hat
    'oh': 46,  // Opened Hi-hat
    'cc': 49,  // Crash Cymbal
    'rc': 51   // Ride Cymbal
};



export function generateMusicFile(music: Music,filePath: string, destination: string | undefined): string {
    const data = extractDestinationAndName(filePath, destination);
    const generatedFilePath = `${path.join(data.destination, data.name)}.py`;

    const fileNode = new CompositeGeneratorNode();
    compile(music, fileNode)


    if (!fs.existsSync(data.destination)) {
        fs.mkdirSync(data.destination, {recursive: true});
    }
    fs.writeFileSync(generatedFilePath, toString(fileNode));
    return generatedFilePath;
}


function compile(music: Music, fileNode: CompositeGeneratorNode): void {
    fileNode.append(
        'from midiutil import MIDIFile\n'

    );

    for (const track_set of music.trackSet) {
        compileTrackSet(track_set, music.tempo, track_set.time_signature , fileNode);
    }
    generateMidiFile(music.name, fileNode);


    // TODO : Est ce encore utile ?
    //generateMidiFile(music.tracks, fileNode, music.name);
}

function compileTrackSet(track_set: TrackSet, tempo: any, time_signature: TimeSignature, fileNode: CompositeGeneratorNode) {

    const number_of_tracks = track_set.track.length;
    fileNode.append(
        `midi = MIDIFile(${number_of_tracks})\n`
    );

    for(let i = 0; i < track_set.track.length; i++){
       
        fileNode.append(
            `midi.addTempo(0, 0, ${tempo})\n`
        );
        fileNode.append(
            `time_signature = ( ${time_signature.numerator} ,  ${time_signature.denominator} )\n`
        );
        fileNode.append(
            `midi.addTimeSignature(0, 0, *time_signature, 24)\n`
        );

        compileTrack(track_set.track[i], i, fileNode);

    }


}

function compileTrack(track: Track, trackNumber: any, fileNode: CompositeGeneratorNode): void {
    const instrumentNumber = compileInstrument(track.instrument.name.toUpperCase(), fileNode);

    for (const trackPart of track.parts) {
        fileNode.append(
            `midi.addProgramChange(${trackNumber}, ${trackNumber}, 0, ${instrumentNumber})\n`
        );

        const repeatCount = trackPart.repeat || 1;
        for (let i = 0; i < repeatCount; i++) {
            if (track.instrument.name.toUpperCase() === 'DRUM') {
                compileDrumNote(trackPart.notes, instrumentNumber, trackNumber, i, fileNode);
            } else {
                compileNote(trackPart.notes, instrumentNumber, trackNumber, i, fileNode);
            }
        }
    }
}



function compileInstrument(instrument:String ,fileNode : CompositeGeneratorNode ) : number {

    // TODO : return number of chanel

    switch (instrument) {
        case 'PIANO':
            return 0;
        
        case 'GUITAR':
            return 25; // Acoustic Guitar (steel)
        
        case 'DRUM':
            return 9;
        
        default:
            return 0; // Handle other instrument cases or return an empty string if none matches
    }
}



function compileNote(notes: Note[],instrument_number:number, track_number : any, i:number, fileNode: CompositeGeneratorNode): void {
    for(const note of notes){
        const pitchValue = noteMap[note.pitch.toUpperCase()];
        if (pitchValue === undefined) {
            throw new Error(`Unknown pitch ${note.pitch}`);
        }

        else{
            const decimal = note.position.n1+i;
            fileNode.append(

            `midi.addNote(${track_number}, ${instrument_number}, ${pitchValue}, ${decimal+`.`+note.position.n2} ,${note.duration}, ${note.volume})\n`);
        }
        
    }
}



function compileDrumNote(notes: Note[],instrument_number:number, track_number : any, i:number, fileNode: CompositeGeneratorNode): void {
    for(const note of notes){
        const pitchValue = drumMap[note.pitch];
        console.log(note.pitch.toUpperCase())
        if (pitchValue === undefined) {
            throw new Error(`Unknown pitch ${note.pitch}`);
        }

        else{
            const decimal = note.position.n1+i;
            fileNode.append(
            `midi.addNote(${track_number}, ${instrument_number}, ${pitchValue},${decimal+`.`+note.position.n2} ,${note.duration}, ${note.volume})\n`);
        }
        
    }
}




function generateMidiFile(name:String, fileNode:CompositeGeneratorNode) {
    fileNode.append(
        `with open("./output/${name}.mid", "wb") as output_file:\n`
    );
    fileNode.append(
        `   midi.writeFile(output_file)\n`
    );
}




