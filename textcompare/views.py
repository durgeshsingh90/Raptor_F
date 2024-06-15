from django.shortcuts import render
import difflib

def compare_texts(request):
    context = {}
    if request.method == 'POST':
        text1 = request.POST.get('text1', '').strip()
        text2 = request.POST.get('text2', '').strip()

        diff = difflib.ndiff(text1.splitlines(), text2.splitlines())
        highlighted_text1 = []
        highlighted_text2 = []

        for line in diff:
            if line.startswith('+ '):
                highlighted_text2.append(f'<span class="added">{line[2:]}</span>')
            elif line.startswith('- '):
                highlighted_text1.append(f'<span class="removed">{line[2:]}</span>')
            elif line.startswith('? '):
                # This line indicates which characters are different within a line
                continue
            else:
                highlighted_text1.append(line[2:])
                highlighted_text2.append(line[2:])

        context = {
            'text1': '\n'.join(highlighted_text1),
            'text2': '\n'.join(highlighted_text2),
        }

    return render(request, 'textcompare/compare_texts.html', context)

