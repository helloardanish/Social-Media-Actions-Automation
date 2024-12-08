import PySimpleGUI as sG
from Instagram.InstaFollowers import InstaFollowers
from conf.MyLogger import customlogger

logger = customlogger("Main")

def main():
    # Create the coordinate insta_followers instance
    insta_followers = InstaFollowers()

    # Define the options
    followers_options = [1, 5, 10, 20, 50, 100, 250, 500]

    # Set the theme
    sG.theme('DarkBlue3')

    # Define the layout
    layout = [
        [sG.Text("Select an option:")],
        [sG.Listbox(values=followers_options, size=(50, len(followers_options)), key="SELECTED_OPTION", enable_events=True)],
        [sG.Text('Remove Insta Followers', font=('Helvetica', 16))],
        [sG.Text('Click Start to start removing insta followers')],
        [sG.Button('Start', key='-START-', size=(10, 1)),
         sG.Button('Scroll', key='-SCROLL-', size=(10, 1), disabled=True),
         sG.Button('Stop', key='-STOP-', size=(10, 1), disabled=True),
         sG.Button('Exit', key='-EXIT-', size=(10, 1))]
    ]

    # Create the window
    window = sG.Window('Remove Insta Followers', layout, finalize=True)

    # Event loop
    while True:
        event, values = window.read(timeout=100)

        if event == sG.WIN_CLOSED or event == '-EXIT-':
            insta_followers.clean_up()
            break
        elif event == '-START-':
            window['-START-'].update(disabled=True)
            window['-STOP-'].update(disabled=False)
            selected_option = values["SELECTED_OPTION"]
            if not selected_option:
                logger.info("Please select an option!")
                window['-START-'].update(disabled=False)
                break
            elif selected_option[0]==1:
                logger.info("Please select other option!")
            else:
                logger.info(f"{selected_option[0]} followers will be removed")
                insta_followers.start(selected_option[0]//5)
            window['-START-'].update(disabled=False)
        elif event == '-SCROLL-':
            window['-START-'].update(disabled=True)
            window['-STOP-'].update(disabled=True)
            # insta_followers.scroll(5)
            window['-START-'].update(disabled=False)
            window['-STOP-'].update(disabled=False)

        elif event == '-STOP-':
            window['-START-'].update(disabled=False)
            window['-STOP-'].update(disabled=True)
            # TODO stop the running method

    window.close()

if __name__ == "__main__":
    main()