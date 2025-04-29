class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        pattern:
            curr_line = []
            iterate on words
                slots = curr_line - 1
                (slots + 1) -> normal spaces that should be there in a line if new_word is added
                if curr_line_text_length + slots + 1 + new_word > maxwidth:
                    # save curr_line
                    gaps = maxWidth - curr_line_text_length
                    if slots > 0:
                        # k words, k-1 slots -> k-1 gaps
                        # if more gaps, (k-1)*m + residue gap
                        space_bet_word, extra_space = divmod(gaps, slots)
                        # build new curr line with space_bet_word
                        # add extra_space  to begining
                    curr_line = [newword]
                build curr_line

        """
        result = []
        curr_line = []
        curr_line_length = 0

        for word in words:
            slots = len(curr_line) - 1

            if curr_line_length + slots + 1 + len(word) > maxWidth:
                gaps = maxWidth - curr_line_length
                if slots > 0:
                    # many words in curr_line

                    space_bet_word, extra_space = divmod(gaps, slots )
                    new_curr_line = [curr_line[0]]
                    if not extra_space:
                        for i in range(1, len(curr_line)):
                            new_curr_line += [' '] * space_bet_word + [curr_line[i]]
                    else:
                        empty_list = [' ']
                        for i in range(1, len(curr_line)):
                            # extra_space = 2
                            # 0 1 2
                            if i-1 < extra_space:
                                new_curr_line += (
                                    [' '] * space_bet_word + empty_list + [curr_line[i]]
                                )
                            else:
                                new_curr_line += (
                                    [' '] * space_bet_word + [curr_line[i]]
                                )
                else:
                    new_curr_line = curr_line + [' ']*gaps

                result.append(''.join(new_curr_line))
                curr_line = [word]
                curr_line_length = len(word)
            else:
                curr_line.append(word)
                curr_line_length += len(word)
        
        if curr_line:
            gaps = maxWidth - curr_line_length
            new_curr_line = [curr_line[0]]
            for i in range(1, len(curr_line)):
                new_curr_line += [' '] + [curr_line[i]]
                gaps -= 1
            
            new_curr_line = new_curr_line + [' ']*gaps

            result.append(''.join(new_curr_line))

        return result


