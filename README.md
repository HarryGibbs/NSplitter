# NSplitter
<b><h2>Description:</h2></b>
<p>
NSplitter is a Python program which takes an alignment of the coding regions of a set of homologous genes or genomes.  It identifies the non-silent (non-synonymous), silent (synonymous) and unchanged codons, and outputs them in three separate files; "ns", "s" and "u". These, like the input alignment are in FAS/FASTA/txt file format, allowing them to be opened by programs such as BioEdit and text editing software such as Microsoft Word and Notepad. NSplitter also outputs a fourth file called 'position-values.txt' which contains a string of values, '0', '1' or '2', for each codon in the alignment; '0' means that that codon position has no-differences in all the sequences, '1' means that there is at least one or more changes in that codon position, but all are silent, and '2' meaning that at least one of the changes in that codon position is non-silent irrespective of whether there are any silent changes too. This program is not specific to Windows or Mac, and only requires the download of the program and the presence of Python (steps detailed below).<br/>
For a benchmark, this program has compared an alignment of 20 sequences, each being 30,000 bases long, in under 10 seconds.
</p>

<b><h2>Installation:</h2></b>
<p>
First, Python must be installed. It can be found at https://www.python.org/downloads/. When downloaded, there will be a setup prompt to help set it up on your computer.
Once this Python shell is successfully installed, download the NSplitter file system from the GitHub repository. Make sure that when it is downloaded, you have extracted the files and put them somewhere accessible within your computer (when moving the file system, keep all the files and folders contained within the folder, which is called “NSplitter” by default).  
</p>

<b><h2>Usage:</h2></b>
<p>Place the alignment to be split into the “input” folder. Make sure this file complies with the desired nomenclature, which can be seen at the end of this file. The Python program reads either T (thymine) or U (uracil) as the same nucleotide. All genes/genomes within the ‘input file’ must be the same length, and NSplitter assumes that they have been aligned with hyphens or tildas (either --- or ~~~). There also must be only a single input file within the input folder, this file and its name must be in *.fas or *.txt format.<br/><br/>
<b><i>Windows only:</i></b> If the input file is properly configured, open the “run.py” file with Python. This can be done by right-clicking on the 'run' file, clicking “Open With”, if “Python” appears as an option, click this option.  If it does not appear than click “Choose another app” and then “More apps” and find it within there.<br/><br/>
<b><i>Mac only:</i></b> If the input file is properly configured, open the “run.py” file with Python Launcher (the version should be around 3.8.5, but may differ slightly). This can be done by right-clicking on the run file, clicking “Open With”, if “Python Launcher” is an option within “Open With”, click this option. If not click “Other” and then find “Python Launcher” within the “Applications” folder, in a folder called “Python 3.8” (or similar). On first time use, it may prompt you to let it access files, allow it.<br/><br/>
For both Mac and Windows a black box will appear with a growing string of numbers, once the NSplitting is complete, it will close itself. The new files of ns.txt, s.txt, u.txt and position-values.txt will have been updated. These “output files” can be copied and pasted elsewhere, but do not move them, as the program requires a copy of these 4 output files (with their correct names) in the NSplitter file. If you encounter an error in this process or problem in this guide, please refer to the section below.</p>


<b><h2>Help! and Errors:</h2></b>
<p><b>Incorrect file length or code didn’t run:</b> All sequences within the “input file” must be the exactly the same length, the program will not work properly and will most likely just stop running if the sequences are not aligned. If the genetic code is properly aligned, please refer to point 3 of “Help! and Errors”. <br/><br/>
<b>Incorrect coding of codon:</b> If a there is a typo or just an incorrect codon within the file, the code will stop running and tell you what was incorrect within the file. You can then use BioEdit to find that fault, which, most commonly will be that the sequences include redundant nucleotide codes (e.g. Y = C or T or R = A or G, etc) and not the primary code - see below.<br/><br/>
<b>Installation or use of either Python or NSplitter didn’t work:</b> If there were any problems, please email me at harrymanninggibbs@gmail.com . I will try to fix the issue as quickly as possible.</p>

<b><h2>Required nomenclature:</h2></b>
<p>
1 : ["GCT", "GCC", "GCA", "GCG", "GCU"] encoding alanine (A),<br/>
2 : ["TGT", "TGC", "UGU", "UGC"] encoding cysteine (C),<br/>
3 : ["GAT", "GAC", "GAU"] encoding aspartic acid (D),<br/>
4 : ["GAA", "GAG"] encoding glutamic acid (E),<br/>
5 : ["TTT", "TTC", "UUU", "UUC"] encoding phenylalanine (F),<br/>
6 : ["GGT", "GGC", "GGA", "GGG", "GGU"] encoding glycine (G),<br/>
7 : ["CAT", "CAC", "CAU"] encoding histidine (H),<br/>
8 : ["ATT", "ATC", "ATA", "AUU", "AUC", "AUA"] encoding isoleucine (I),<br/>
9 : ["AAA", "AAG"] encoding lysine (K),<br/>
10 : ["TTG", "TTA", "CTT", "CTC", "CTA", "CTG", "UUG", "UUA", "CUU", "CUC", "CUA", "CUG"], encoding leucine (L),<br/>
11 : ["ATG", "AUG"] encoding methionine (M),<br/>
12 : ["AAT", "AAC", "AAU"] encoding asparagine (N),<br/>
13 : ["CCT", "CCC", "CCA", "CCG", "CCU"] encoding proline (P),<br/>
14 : ["CAA", "CAG"] encoding glutamine (Q),<br/>
15 : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG", "CGU"] encoding arginine (R),<br/>
16 : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC", "UCU", "UCC", "UCA", "UCG", "AGU"] encoding serine (S),<br/>
17 : ["ACT", "ACC", "ACA", "ACG", "ACU"] encoding threonine (T),<br/>
18 : ["GTT", "GTC", "GTA", "GTG", "GUU", "GUC", "GUA", "GUG"] encoding valine (V),<br/>
19 : ["TGG", "UGG"] encoding tryptophan (W),<br/>
20 : ["TAT", "TAC", "UAU", "UAC"] encoding tyrosine (Y),<br/>
21 : ["TAA", "TAG", "UAA", "UAG"] encoding 'termination' (*),<br/>
22 : ["---", "~~~"]<br/>
</p>

