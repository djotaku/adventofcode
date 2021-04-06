def input_per_line(file)
    lines = File.readlines(file)
    cleaned_up_lines = []
    for line in lines
        cleaned_up_lines.append(line.strip)
    end
    return cleaned_up_lines
end
