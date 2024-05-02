'''
=================================================================================================
Tidal AutoExport	: Automated export Tidal shared links
-------------------------------------------------------------------------------------------------
Author			    : SunL0w
-------------------------------------------------------------------------------------------------
Version			    : 1.0
-------------------------------------------------------------------------------------------------
Github			    : https://github.com/SunL0w/Tidal-AutoDL
=================================================================================================

/!\\ Disclaimer : 
This script is for educational use. 
I am not responsible if it is used to commit illegal actions.

=================================================================================================

                   GNU GENERAL PUBLIC LICENSE
                    Version 3, 29 June 2007

    Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
    Everyone is permitted to copy and distribute verbatim copies
    of this license document, but changing it is not allowed.

                         Preamble

    The GNU General Public License is a free, copyleft license for
    software and other kinds of works.

    The licenses for most software and other practical works are designed
    to take away your freedom to share and change the works.  By contrast,
    the GNU General Public License is intended to guarantee your freedom to
    share and change all versions of a program--to make sure it remains free
    software for all its users.  We, the Free Software Foundation, use the
    GNU General Public License for most of our software; it applies also to
    any other work released this way by its authors.  You can apply it to
    your programs, too.

    When we speak of free software, we are referring to freedom, not
    price.  Our General Public Licenses are designed to make sure that you
    have the freedom to distribute copies of free software (and charge for
    them if you wish), that you receive source code or can get it if you
    want it, that you can change the software or use pieces of it in new
    free programs, and that you know you can do these things.

    To protect your rights, we need to prevent others from denying you
    these rights or asking you to surrender the rights.  Therefore, you have
    certain responsibilities if you distribute copies of the software, or if
    you modify it: responsibilities to respect the freedom of others.

    For example, if you distribute copies of such a program, whether
    gratis or for a fee, you must pass on to the recipients the same
    freedoms that you received.  You must make sure that they, too, receive
    or can get the source code.  And you must show them these terms so they
    know their rights.

    Developers that use the GNU GPL protect your rights with two steps:
    (1) assert copyright on the software, and (2) offer you this License
    giving you legal permission to copy, distribute and/or modify it.

    For the developers' and authors' protection, the GPL clearly explains
    that there is no warranty for this free software.  For both users' and
    authors' sake, the GPL requires that modified versions be marked as
    changed, so that their problems will not be attributed erroneously to
    authors of previous versions.

    Some devices are designed to deny users access to install or run
    modified versions of the software inside them, although the manufacturer
    can do so.  This is fundamentally incompatible with the aim of
    protecting users' freedom to change the software.  The systematic
    pattern of such abuse occurs in the area of products for individuals to
    use, which is precisely where it is most unacceptable.  Therefore, we
    have designed this version of the GPL to prohibit the practice for those
    products.  If such problems arise substantially in other domains, we
    stand ready to extend this provision to those domains in future versions
    of the GPL, as needed to protect the freedom of users.

    Finally, every program is threatened constantly by software patents.
    States should not allow patents to restrict development and use of
    software on general-purpose computers, but in those that do, we wish to
    avoid the special danger that patents applied to a free program could
    make it effectively proprietary.  To prevent this, the GPL assures that
    patents cannot be used to render the program non-free.

    The precise terms and conditions for copying, distribution and
    modification follow.

-------------------------------------------------------------
'''

def export_tidal_links(source_file, output_file):
    # Open source file in read mode and output file in write mode
    with open(source_file, 'r', encoding='utf-8') as file, open(output_file, 'w', encoding='utf-8') as output:
        # Browse each line in the source file
        for line in file:
            # Search for all occurrences of "https://tidal.com/" in the line
            tidal_links = [link for link in line.split() if link.startswith("https://tidal.com/")]
            # Write all Tidal links found in the output file
            for link in tidal_links:
                output.write(link + '\n')

def remove_duplicates(input_file, output_file):
    # Open input file in read mode
    with open(input_file, 'r', encoding='utf-8') as file:
        # Read all file lines in a list
        lines = file.readlines()

    # Use a set to remove duplicates
    unique_lines = set(lines)

    # Open output file in write mode
    with open(output_file, 'w', encoding='utf-8') as file:
        # Write single lines to output file
        file.writelines(unique_lines)

print()
print("[Tidal AutoExport]")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print()

# Call function to export Tidal links
print("[i] Exporting Tidal links...")
export_tidal_links("source.txt", "tidal_export.txt")

# Call function to delete duplicates
print("[i] Deleting duplicates...")
remove_duplicates("tidal_export.txt", "clean_tidal_export.txt")
