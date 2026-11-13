# Makefile for Textbooks and Workbooks
# Author: Abderraouf Boudjema

.PHONY: all clean textbooks workbooks \
        mechanics-textbook chemistry-textbook math-textbook \
        mechanics-workbook chemistry-workbook math-workbook

all: textbooks workbooks

textbooks: mechanics-textbook chemistry-textbook math-textbook
workbooks: mechanics-workbook chemistry-workbook math-workbook

mechanics-textbook:
	@echo "==> Compiling Principles of Classical Mechanics Textbook..."
	cd textbooks/classical-mechanics && pdflatex -interaction=nonstopmode textbook.tex > /dev/null
	cd textbooks/classical-mechanics && pdflatex -interaction=nonstopmode textbook.tex > /dev/null
	cp -f textbooks/classical-mechanics/textbook.pdf textbooks/classical-mechanics/Principles_of_Classical_Mechanics_Textbook.pdf
	@echo "==> Completed: textbooks/classical-mechanics/Principles_of_Classical_Mechanics_Textbook.pdf"

chemistry-textbook:
	@echo "==> Compiling Structure of Matter Comprehensive Textbook..."
	cd textbooks/structure-of-matter && pdflatex -interaction=nonstopmode textbook.tex > /dev/null
	cd textbooks/structure-of-matter && pdflatex -interaction=nonstopmode textbook.tex > /dev/null
	cp -f textbooks/structure-of-matter/textbook.pdf textbooks/structure-of-matter/Structure_of_Matter_Comprehensive_Textbook.pdf
	@echo "==> Completed: textbooks/structure-of-matter/Structure_of_Matter_Comprehensive_Textbook.pdf"

math-textbook:
	@echo "==> Compiling University Mathematics I Comprehensive Textbook..."
	cd textbooks/university-mathematics-i && pdflatex -interaction=nonstopmode textbook.tex > /dev/null
	cd textbooks/university-mathematics-i && pdflatex -interaction=nonstopmode textbook.tex > /dev/null
	cp -f textbooks/university-mathematics-i/textbook.pdf textbooks/university-mathematics-i/University_Mathematics_I_Comprehensive_Textbook.pdf
	@echo "==> Completed: textbooks/university-mathematics-i/University_Mathematics_I_Comprehensive_Textbook.pdf"

mechanics-workbook:
	@echo "==> Compiling Mechanics Complete Exercise Book..."
	cd workbooks/classical-mechanics && pdflatex -interaction=nonstopmode main.tex > /dev/null
	cd workbooks/classical-mechanics && pdflatex -interaction=nonstopmode main.tex > /dev/null
	cp -f workbooks/classical-mechanics/main.pdf workbooks/classical-mechanics/Mechanics_of_a_Material_Point_Complete_Exercise_Book.pdf
	@echo "==> Completed: workbooks/classical-mechanics/Mechanics_of_a_Material_Point_Complete_Exercise_Book.pdf"

chemistry-workbook:
	@echo "==> Compiling Structure of Matter Complete Exercise Book..."
	cd workbooks/structure-of-matter && pdflatex -interaction=nonstopmode main.tex > /dev/null
	cd workbooks/structure-of-matter && pdflatex -interaction=nonstopmode main.tex > /dev/null
	cp -f workbooks/structure-of-matter/main.pdf workbooks/structure-of-matter/Structure_of_Matter_Complete_Exercise_Book.pdf
	@echo "==> Completed: workbooks/structure-of-matter/Structure_of_Matter_Complete_Exercise_Book.pdf"

math-workbook:
	@echo "==> Compiling University Mathematics I Complete Exercise Book..."
	cd workbooks/university-mathematics-i && pdflatex -interaction=nonstopmode main.tex > /dev/null
	cd workbooks/university-mathematics-i && pdflatex -interaction=nonstopmode main.tex > /dev/null
	cp -f workbooks/university-mathematics-i/main.pdf workbooks/university-mathematics-i/University_Mathematics_I_Complete_Exercise_Book.pdf
	@echo "==> Completed: workbooks/university-mathematics-i/University_Mathematics_I_Complete_Exercise_Book.pdf"

clean:
	@echo "==> Cleaning LaTeX auxiliary build files..."
	find . -type f \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.fdb_latexmk" -o -name "*.fls" -o -name "*.synctex.gz" \) -delete
	@echo "==> Clean complete."
