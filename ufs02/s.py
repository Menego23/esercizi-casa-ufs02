def count_html_elements(corrieredellasera):
    class_count = 0
    link_count = 0
    img_count = 0
    
    with open('corrieredellasera.html', 'r') as f:
        for line in f:
            if 'class=' in line:
                class_count += 1
            if '<a ' in line:
                link_count += 1
            if '<img ' in line:
                img_count += 1
    
    report = f'Classi di stile: {class_count}\nLink: {link_count}\nImmagini: {img_count}'
    
    with open('report.txt', 'w') as f:
        f.write(report)

count_html_elements('corrieredellasera.html')
