#include <stdio.h>
#include <sys/stat.h>
#include <direct.h>
#include <io.h>
#include <time.h>

int main() {
    FILE *fp;
    char file[100], newfile[100], text[256];
    struct stat info;
    int ch;

    while (1) {
        printf("\n=== File Handling Menu ===\n");
        printf("1. Write to File\n");
        printf("2. Read File\n");
        printf("3. Create Directory\n");
        printf("4. Overwrite File\n");
        printf("5. Rename File\n");
        printf("6. Get File Metadata\n");
        printf("7. Search and Overwrite File\n");
        printf("8. Delete File\n");
        printf("9. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &ch);
        getchar();

        switch (ch) {

        case 1:
            printf("Enter filename: ");
            scanf("%99s", file);
            getchar();

            fp = fopen(file, "w");
            if (fp == NULL) {
                printf("Cannot create file.\n");
                break;
            }

            printf("Enter content: ");
            fgets(text, sizeof(text), stdin);
            fprintf(fp, "%s", text);
            fclose(fp);
            printf("Written successfully.\n");
            break;

        case 2:
            printf("Enter filename: ");
            scanf("%99s", file);

            fp = fopen(file, "r");
            if (fp == NULL) {
                printf("File not found.\n");
                break;
            }

            printf("\nFile Contents:\n");
            while (fgets(text, sizeof(text), fp))
                printf("%s", text);

            fclose(fp);
            break;

        case 3:
            printf("Enter directory name: ");
            scanf("%99s", file);

            if (mkdir(file) == 0)
                printf("Directory created successfully.\n");
            else
                printf("Directory already exists or cannot be created.\n");

            break;

        case 4:
            printf("Enter filename: ");
            scanf("%99s", file);
            getchar();

            fp = fopen(file, "w");
            if (fp == NULL) {
                printf("Cannot open file.\n");
                break;
            }

            printf("Enter new content: ");
            fgets(text, sizeof(text), stdin);
            fprintf(fp, "%s", text);
            fclose(fp);
            printf("File overwritten successfully.\n");
            break;

        case 5:
            printf("Enter old filename: ");
            scanf("%99s", file);
            printf("Enter new filename: ");
            scanf("%99s", newfile);

            if (rename(file, newfile) == 0)
                printf("File renamed successfully.\n");
            else
                printf("Rename failed.\n");

            break;

        case 6:
            printf("Enter filename: ");
            scanf("%99s", file);

            if (stat(file, &info) == 0) {
                printf("File Size: %lld bytes\n", (long long)info.st_size);
                printf("Permissions: %o\n", info.st_mode);
                printf("Last Modified: %s", ctime(&info.st_mtime));
            } else {
                printf("File not found.\n");
            }

            break;

        case 7:
            printf("Enter filename: ");
            scanf("%99s", file);

            if (access(file, F_OK) == 0) {
                fp = fopen(file, "w");
                fprintf(fp, "File found and overwritten.\n");
                fclose(fp);
                printf("File found and overwritten.\n");
            } else {
                printf("File not found.\n");
            }

            break;

        case 8:
            printf("Enter filename: ");
            scanf("%99s", file);

            if (remove(file) == 0)
                printf("File deleted successfully.\n");
            else
                printf("File not found.\n");

            break;

        case 9:
            printf("Exiting...\n");
            return 0;

        default:
            printf("Invalid choice.\n");
        }

        printf("\nPress Enter to continue...");
        getchar();
    }

    return 0;
}