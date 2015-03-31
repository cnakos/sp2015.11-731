Machine Translation HW #3
cnakos

This homework proved stubborn; even getting the baseline was difficult.  My implementations would run into one of three bugs:
1) One or more sentences would not align.  Often this was a result of flubbed stack assignment, but many instances were untraceable for me.
2) The final stack would be empty.  The decoder would somehow work its way into a dead end, even with large stack sizes.
3) The translations they produced were worse than the default.  Typically this led to increasingly worse scores with large stack sizes.

The particulars have blurred together, but various from-scratch attempts at modifying the default code met with the same bugs.
For a while I thought the problem was future cost estimation, but this only caused worse behavior.

My best result was a simple implementation, only allowing switching if f[i:j] was a phrase, that got halfway to the baseline.
Though I had tried higher stack sizes on more elaborate approaches, I forgot to try it on this version.
Eventually I figured out that increasing the stack size to 10 maximized this approach's score at the baseline value.

I then tried three ways to extend this implementation for a slight improvement in points.
1) Low-hanging fruit.  The decoder would check for splits of length two of f[j:k] that produced better scores than f[j:k] would produce as a unit.
2) Extra permutation.  The decoder would repeat the process and add a third phrase to the mix, alongside three new reorderings.
3) Depth within stack entries.  The decoder would store up to d hypotheses for each lm_state in each stack.

Properly debugged, the first approach yielded a minor improvement of 5 points over the baseline.
The other two approaches had no tangible effect, at least during my tests.

And for the sake of time, that's where I'll leave it.